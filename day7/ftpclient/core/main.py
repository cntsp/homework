import socket
import os
import json
import hashlib
from authentication import User
import commands


class FtpClient(object):
    """
    define the ftpclient class
    """

    def __init__(self, host="localhost", port=9999):
        self.client = socket.socket()
        self.host = host
        self.port = port
        self.client_user = User()
        self.connection(self.host, self.port)

    def connection(self, *args):
        # print(args[0], args[1])
        # self.client = socket.socket()
        c1 = self.client.connect((args[0], args[1]))
        # print("line25: ", c1)
        
        if not c1:
            username = self.client_user.login(self.client)
            if username:
                commands.cmd.help()
                self.handle(username)
                self.client.close()
        else:
            print("the client failed to connect to the server")

    def handle(self, username):
        """
        analyze the data entered, in order to get command and filename.
        :return:
        """
        # 实例化一个所有命令的对象
        command1 = commands.cmd(self.client)
        flag = True
        home_directory = "/home/%s" % username
        current_directory = home_directory
        while flag:
            # print("current_directory:", current_directory)
            while True:
                enter_data = input("\033[32;1mftp>[%s]\033[0m" % current_directory).strip()
                if len(enter_data) > 0:
                    enter_data_tuple = enter_data.split()
                    break
            if enter_data_tuple[0].startswith('put') or enter_data_tuple[0].startswith('get'):
                command = enter_data_tuple[0]
                filename = enter_data_tuple[1]
                if hasattr(command1, "cmd_{}".format(command)):
                    # print("@@@@:command1", commands.cmd(self.client))
                    # filepath = up_down_file_path + "/" + filename
                    if os.path.isfile(filename) or enter_data_tuple[0].startswith('get') :
                        # print("ftpclient line 38:")
                        try:
                            size = os.stat(filename).st_size
                        except FileNotFoundError as e:
                            size = 0
                        msg_dict = {
                            "username": username,
                            "action": command,
                            "filename": filename,
                            "file_size": size,
                            "override": True,
                            "home_directory": home_directory,
                            "current_directory": current_directory
                        }
                        func = getattr(command1, "cmd_{}".format(command))
                        # print("line 68", func)
                        current_directory = func(msg_dict)
                    else:
                        print("your operate {} file is not exist!".format(filename))
            elif enter_data_tuple[0].startswith('ls') or enter_data_tuple[0].startswith('cd') or enter_data_tuple[0].startswith('mkdir'):
                try:
                    command = enter_data_tuple[0]
                    second_parameter = enter_data_tuple[1]
                    # print("line 71:",command, second_parameter)
                    msg_dict = {
                        "action": command,
                        "second_parameter": second_parameter,
                        "username": username,
                        "home_directory": home_directory,
                        "current_directory": current_directory
                    }
                    # print("@@@ line 57:")
                except IndexError as e:
                    print("your enter commands has a false:", e)
                if hasattr(command1, "cmd_{}".format(enter_data_tuple[0])):
                    func = getattr(command1, "cmd_{}".format(enter_data_tuple[0]))
                    current_directory = func(msg_dict)
                    # print("### current_directory:", current_directory)    
            elif enter_data_tuple[0].startswith('exit'):
                flag = False
            else:
                print("\033[32;1mthe data of your enter has error! please Usage: \033[0m")
                commands.cmd.help()


if __name__ == "__main__":
    f1 = FtpClient()
