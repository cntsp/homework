import os
import json
import hashlib
# 文件所在绝对路径的上上级目录
file_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 定义客户端文件的上传下载的目录
up_down_file_path = os.path.join(file_directory, "home")


class cmd():
    def __init__(self, client):
        self.client =client
        pass

    def cmd_mkdir(self, msg_dict):
        self.client.send(json.dumps(msg_dict).encode())
        server_response = self.client.recv(1024)
        if server_response:
            print("server_reponse.decode:", server_response.decode())
            print("%s direcotry has created successfully!" % msg_dict["second_parameter"])
        return server_response.decode()
    def cmd_cd(self, msg_dict):
        self.client.send(json.dumps(msg_dict).encode())
        server_response = self.client.recv(1024)
        # print("line 21:", server_response)
        if server_response.startswith(b"sorry"):
            print("\033[31;1m警告：\033[0m", server_response.decode())
            server_response = msg_dict["current_directory"]
            server_response = server_response.encode()
        return server_response.decode()
        
    def cmd_put(self, msg_dict):
        self.client.send(json.dumps(msg_dict).encode())
        server_response = self.client.recv(1024)
        print("line 34:", server_response)
        server_response_data = server_response.decode() # 
        print("in the cmd_put:",server_response_data)
        server_response_data = json.loads(server_response_data)
        # print("the server response:", server_response)
        # if server_response.startswith(b'ok'):
        if server_response_data["file_status"] == "noexists":
            # print("the client line 64:", server_response)
            client_md5 = hashlib.md5()
            send_data = 0
            with open(msg_dict["filename"], 'rb') as f:
                for line in f:
                    try:
                        # print("the client line 66:", line)
                        client_md5.update(line)
                        self.client.send(line)
                        send_data += len(line)
                        self.prograss_bar(msg_dict["file_size"], send_data, "上传")
                    except KeyboardInterrupt as e:
                        print("\033[31;1m%s\033[0m" % e)
                        print("keyboardinterrupt")
                        information_dict = {
                            "interrupt_client_md5": client_md5,
                            "send_byte_data": send_data,
                            "filename": msg_dict['filename'] 
                        }
                        self.client.send("KeyboardInterrupt".encode())
                        return msg_dict["current_directory"]
                client_md5_value = client_md5.hexdigest()
            server_md5_value = self.client.recv(1024)
            print("the filename has put done!")
            print("the client_md5 value is:", client_md5_value)
            print("the server_md5 value is:", server_md5_value.decode())
        elif server_response_data['file_status'] == 'exists':
            seek_size = server_response_data['seek_size']
            send_data =0
            with open(msg_dict["filename"], 'rb') as f:
                f.seek(seek_size)
                try:
                    for line in f:
                        self.client.send(line)
                        send_data += len(line)
                        self.prograss_bar(msg_dict["file_size"]-seek_size, send_data, "上传")
                except Exception as e:
                    print("\033[31;1m告警:\033[0m", e)
                else:
                    print("\033[33;1m断点续传完成!\033[0m")
        else:
            print("\033[31;1m警告：%s\033[0m" % server_response.decode())
        return msg_dict["current_directory"]

    def cmd_get(self, msg_dict):
        self.client.send(json.dumps(msg_dict).encode())
        # print("in the cmd_get:")
        server_response = self.client.recv(1024)
        # print("the server response:", server_response)
        file_size = json.loads(server_response.decode())
        received_data = 0
        client_md5 = hashlib.md5()
        self.client.send(b"the client has ready!")
        send_data = 0
        file_abs_path = up_down_file_path + "/" + msg_dict["filename"]
        with open(file_abs_path, 'wb') as f:
            while received_data < file_size:
                data = self.client.recv(1024)
                client_md5.update(data)
                received_data += len(data)
                # data = re.sub('\\r', ' ', data.decode())
                f.write(data)
                send_data += len(data)
                self.prograss_bar(file_size, send_data, "下载")
                # server_md5.update(data.encode())
                print("received_data, file_size", received_data, file_size)
            print("the client 102 @@@:")
            client_md5_value = client_md5.hexdigest()
            self.client.send("the client has get file done!".encode())
            server_md5_value = self.client.recv(1024)
        print("client_md5_value:", client_md5_value)
        print("server_md5_value:", server_md5_value.decode())
        return msg_dict["current_directory"]

    def prograss_bar(self, all_data, received_data, active):
        all_data_m = all_data / 1024 / 1024
        i1 = received_data * 50 / all_data
        f1 = received_data / all_data * 100
        if all_data_m < 1.0:
            print("start send, [File size]:{} 字节".format(all_data))
            print('\r' + '[%s进度]:%s%.2f%%' % (active, '>' * int(i1), float(f1)))
        else:
            received_data = received_data / 1024 / 1024
            i1 = received_data * 50 / all_data_m
            file_size = "%.2f M" % all_data_m
            print("start send, [File size]: {}".format(file_size))
            print('\r' + '[%s进度]:%s%.2f%%' % (active, '>' * int(i1), float(f1)))

    def cmd_ls(self, msg_dict):
        self.client.send(json.dumps(msg_dict).encode())
        server_response = self.client.recv(1024)
        print("in cmd_ls function server_response: ", server_response.decode())
        return msg_dict["current_directory"]
    
    def cmd_exit(self):
        return False

    @classmethod
    def help(cls):
        msg = """ftp help commands, Usage:
              put filename
              get filename
              ls -lh
              mkdir directoryname
              cd directoryname
              pwd
              exit
          """
        print(msg)
