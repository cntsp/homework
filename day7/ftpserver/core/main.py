#!/usr/bin/python
#-*-coding:utf8-*-

import socketserver
import json
import os
import re
import hashlib
import platform
from . import user

db_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our servere.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        while True:
            try:
                print("line 21:")
                self.data = self.request.recv(1024).strip()
                print("self.data:", self.data)
                print("line 27")
            except ConnectionResetError as e:
                print("the client has interrupt!")
            # receive the bytes data , then change it to the data of dict format
            msg_dict = json.loads(self.data.decode())
            print("the server line 26:", msg_dict)
            if hasattr(self, "cmd_{}".format(msg_dict["action"])):
                func = getattr(self, "cmd_{}".format(msg_dict["action"]))
                func(msg_dict)

    def cmd_mkdir(self, msg_dict):
        """
        create dirctory in the ftp server
        """
        dir = msg_dict["second_parameter"]
        # dir_path = "/home/%s/%s" % (msg_dict["username"],dir)
        dir_path = msg_dict["current_directory"] + '/' + msg_dict["second_parameter"]
        os.system("mkdir %s" % dir_path)
        self.request.send(msg_dict["current_directory"].encode())
        
    def cmd_cd(self, msg_dict):
        if msg_dict["second_parameter"] == ".." and  msg_dict["home_directory"] ==  msg_dict["current_directory"]:
            self.request.send(b"sorry, you are forbidden to leave the home directory!")
        
        elif msg_dict["second_parameter"] == ".." and msg_dict["home_directory"] != msg_dict["current_directory"]:
            bash_path = msg_dict["current_directory"]
            path = os.path.dirname(bash_path)
            print("in the cmd_cd func", path)
            os.system("cd %s" % path)
            self.request.send(path.encode())
        else:
            try:
                print("line 62:#####")
                bash_path = msg_dict["current_directory"] + '/' + msg_dict["second_parameter"]
                os.system("cd %s" % bash_path)
                print("line 65:", bash_path)
                self.request.send(bash_path.encode())
            except Exception as e:
                print("e", e)
    def cmd_login(self, msg_dict):
        """
        the client login authentication
        :param msg_dict:
        :return: True/False
        """
        print("msg_dict line 41:", msg_dict)
        username = msg_dict["username"]
        password = msg_dict["password"]
        # user_path = "%s\\data\\%s" % (db_path, username)
        # user_path = os.system("mkdir %s" % user_path)
        if platform.platform().startswith("Linux"):
            db_file_path = db_path + "/data/user.json"
        else:
            db_file_path = db_path + "\\data\\user.json"

        with open(db_file_path, "r") as f:
            user_information = json.load(f)
            print("line 48:", user_information)
            if username in user_information.keys() and password == user_information[username]["password"]:
                self.request.send(b'ok')
                return True
            else:
                self.request.send(b'notok')
                return False

    def cmd_put(self, msg_dict):
        """
        the client put file to server.
        :param msg_dict: put the inofrmation of the dict format.
        :return:
        """
        filename = msg_dict["filename"]
        filename_path = msg_dict["current_directory"] + '/' + filename
        print("102 line:", filename_path)
        print("103 line:", os.path.isfile(filename_path))
        # input("please wait me:")
        if not os.path.isfile(filename_path):
            print("the server line 36:")
            self.receive_data(msg_dict)
        else:
            filename = msg_dict['filename']
            file_size = msg_dict['file_size']
            received_data = 0
            size = os.stat(filename_path).st_size   # 需要发给客户端，客户端从这个字节位置开始读取上传文件
            file_path = db_path + "/data/" + "user.json"  # 用户信息存放的绝对路径
            with open(file_path, 'r') as f:
                user_information = json.load(f)
            print("line 118:", user_information)
            username = msg_dict["username"]
            remain_quota = float(user_information[username]["remain_quota"].split('M')[0]) * 1024 * 1024
            need_put_size = file_size - size
            if need_put_size < remain_quota:
                # 字典中表示上传文件在服务器上已经存在，客户端需要从文件什么位置 seek 内容
                put_file_stat_information = {"file_status": "exists", "seek_size": size}
                self.request.send(json.dumps(put_file_stat_information).encode())
                filename_abs_path = "%s" % msg_dict["current_directory"] + "/" + filename  # 上传文件的存放的绝对路径
                new_remain_quota = remain_quota - float(need_put_size)   # 此次上传成功后，用户的剩余空间额度/单位为bytes
                new_remain_quota = new_remain_quota / 1024 / 1024  # 此次上传成功后，用户的剩余空间额度/单位为M
                # 把上传文件成功后，剩余的额度写入数据库文件存储
                with open(file_path, 'r') as f:
                    data1 = json.load(f)
                    data1[username]["remain_quota"] = str(new_remain_quota) + 'M'
                with open(file_path, 'w') as f:
                    json.dump(data1, f)
                    
                with open(filename_path, 'wb') as f:
                    f.seek(size)
                    while received_data < need_put_size:
                        data = self.request.recv(1024)
                        received_data += len(data)
                        f.write(data)
                    
                    
    def receive_data(self, msg_dict):
        filename = msg_dict["filename"]
        file_size = msg_dict["file_size"]
        received_data = 0
        # self.request.send(b'ok, now the client can send file data!')
        print("file_size:", file_size)
        file_path = db_path + "/data/" + "user.json"
        with open(file_path, 'r') as f:
            user_information = json.load(f)
        print("line 118:", user_information)
        username = msg_dict["username"]
        remain_quota = float(user_information[username]["remain_quota"].split('M')[0]) * 1024 * 1024
        if file_size < remain_quota:
            put_file_stat_information = {"file_status": "noexists", "seek_size": 0 }
            # self.request.send(b'ok, now the client can send file data!')
            self.request.send(json.dumps(put_file_stat_information).encode())
            filename_abs_path = "%s" % msg_dict["current_directory"] + "/" + filename
            if msg_dict["action"] == "put":
                new_remain_quota = remain_quota - float(file_size)
                new_remain_quota = new_remain_quota / 1024 / 1024
                with open(file_path, 'r') as f:
                    data1 = json.load(f)
                    data1[username]["remain_quota"] = str(new_remain_quota) + 'M'
                with open(file_path, 'w') as f:
                    json.dump(data1, f)
            ctrl_c = "KeyboardInterrupt".encode()
            flag = True
            with open(filename_abs_path, 'wb') as f:
                server_md5 = hashlib.md5()
                while received_data < file_size and flag:
                    data = self.request.recv(1024)
                    if re.search(str(ctrl_c),str(data)):
                        print("line 138:")
                        data = str(data).split(str(ctrl_c))[0]
                        data = data.encode()
                        flag = False
                    received_data += len(data)
                    server_md5.update(data)
                    f.write(data)
                    # server_md5.update(data.encode())
                    print("received_data, file_size", received_data, file_size)
            
                print("the server 62 @@@:")
                server_md5_value = server_md5.hexdigest()
                self.request.send(server_md5_value.encode())
        else:
            print("not enough")
            self.request.send("sorry,remain_quota has not enough!".encode())
         

    def cmd_get(self, msg_dict):
        """
        the client get file from server.
        :param msg_dict:
        :return:
        """
        filename = msg_dict["filename"]
        filename_abs_path = "%s" % msg_dict["current_directory"] + "/" + filename
        # print("in the cmd_get server:", filename_abs_path)
        if os.path.isfile(filename_abs_path):
            # print("@@@@")
            file_size = os.stat(filename_abs_path).st_size
            self.request.send(str(file_size).encode())
            reply = self.request.recv(1024)
            server_md5 = hashlib.md5()
            if reply:
                with open(filename_abs_path, 'rb') as f:
                    for line in f:
                        self.request.send(line)
                        server_md5.update(line)
                server_md5_value = server_md5.hexdigest()
                replay2 = self.request.recv(1024)
                # print("in the cmd_get server:", replay2)
                self.request.send(server_md5_value.encode())

    def cmd_ls(self, msg_dict):
        command = msg_dict["action"]
        options = msg_dict["second_parameter"]
        result = os.popen("cd {} && {} {}".format(msg_dict["current_directory"], command, options)).read()
        print("line 115 result:", result)
        if result == "":
            result = "这是一个空目录!"
        self.request.send(result.encode())
        
def start():
    host, port = "localhost", 9999
    server = socketserver.ThreadingTCPServer((host, port), MyTCPHandler)
    server.serve_forever()
    server.server_close()



if __name__ == "__main__":
    host, port = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((host, port), MyTCPHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    server.server_close()
    # print(platform.platform())


