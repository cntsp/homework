#!-*- coding:utf8 -*-

import json
import os
import sys

db_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class User(object):
    def __init__(self, username="", password="", quota_size="50M", remain_quota="50M", flag=False):
        self.username = username
        self.password = password
        self.quota_size = quota_size
        self.remain_quota = remain_quota
        self.flag = flag

    def login(self):
        while True:
            username = input("please enter your username:").strip()
            password = input("please enter your password:").strip()
            self.username = username
            self.password = password
            data = self.read_user_information()
            if self.username in data.keys() and self.password == data[username][username]:
                print("\033[32;1m welcome login ftp server! \033[0m")
                flag = False
                return True
            else:
                print("\033[31;1m your usernmae or password is false\033[0m")
                flag = True
                return False

    def write_user_information(self):
        """
        create user login information, and write it to db.
        :return:
        """
        self.flag = True
        file_path = db_path + "/data/" + "user.json"
        try:
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    data = {}
                    json.dump(data, f) 
        except Exception as e:
            print(e)
        else:
            with open(file_path, 'r') as f:
                data = json.load(f)
            data[self.username] = {"username": self.username, "password": self.password, "quota_size": self.quota_size, "remain_quota": self.remain_quota}
            with open(db_path + '/data/' + "user.json", "w") as f:
                json.dump(data, f)
        
            
    def read_user_information(self):
        """
        read user login information, and return it
        :return:
        """
        with open(db_path + '/data/' + "user.json", "r") as f:
            data = json.load(f)
        return data

    def create_user_home_directory(self):
        """
        create user home directory
        :return: user's home directory
        """

        home_directory = "/home/" + self.username
        os.system("mkdir %s" % self.username)
        return home_directory


if __name__ == "__main__":

     # 初始化3个ftp用户
     r1 = User("cntsp", "nihaoma", "100M", "100M")
     r1.write_user_information() 

     r2 = User("xiaojie","nihaoma", "100M", "100M")
     r2.write_user_information()
    
     r3 = User("xiaohong", "nihaoma", "50M", "50M")
     r3.write_user_information()


    
