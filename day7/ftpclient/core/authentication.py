import json
import os
import socket
import getpass

db_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class User(object):

    def login(self, socket1):
        # host, port = 'localhost', 9999
        # print("\033[33;1m welcome to login ftp-server!")
        flag = True
        while flag:
            username = input("\033[33;1mplease enter your username:\033[0m")
            password = getpass.getpass("\033[33;1mplease enter your password:\033[0m")
            # if not socket1.connect((host, port)):
            msg_dict = {"username":username, "password": password, "action": "login"}
            socket1.send(json.dumps(msg_dict).encode())
            data = socket1.recv(1024)
            if data == b'ok':
                print("\033[31;1mwelcome to login ftp-server!\033[0m")
                #print("ftp>[/home/%s/]#", username)
                flag = False
                return username
            else:
                flag = True
                print("your username or password has false, please try again!")

    def CreateUser(self):
        """
        Create root
        :return:
        """


if __name__ == "__main__":
    pass
