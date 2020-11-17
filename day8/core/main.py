import os
import sys
import configparser
import commands

config_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(config_path)
config_file = config_path + '\\' + "config.ini"
global d
d = {}

class HostManager(object):
    d = {}
    def __init__(self):
        HostManager.welcome()
        HostManager.first_menu()
        HostManager.host_service_function()

    @classmethod
    def host_service_function(cls):
        function_dict = {0: "exec_shell", 1: "put_file", 2: "exit_system"}
        while True:
            print(""" \033[31;1m输入执行命令和上传文件命令前一定要仔细阅读 readme.md
                0 执行命令
                1 上传文件
                2 退出系统
            \033[0m""")
            user_choose1 = int(input("please enter your choose:").strip())
            if user_choose1 not in function_dict.keys():
                print("\033[31;1myour enter has false,please try again!\033[0m")
                continue
            command = input("\n\033[34;1m请输入相应的命令：\033[0m").strip()
            c1 = commands.Cmd(command, d)
            # print(hasattr(function_dict, user_choose1))
            if hasattr(c1, function_dict[user_choose1]):
                func = getattr(c1, function_dict[user_choose1])
                func()
            else:
                print("您的输入有误，请再次输入！")

    @classmethod
    def first_menu(cls):
        # d = {}
        menu_dict = HostManager.read_config()
        for k, v in menu_dict.items():
            if v["type"] not in d:
                d[v["type"]] = [k]
            else:
                d[v["type"]].append(k)
        # d = {'web_clusters': ['web1', 'web2'], 'db_servers': ['mysql1', 'mysql2']}
        for k, v in enumerate(d.keys()):
            print("\033[32;1m %s %s \033[0m" % (k, v))
        choose_dict = {0: "web_clusters", 1: "db_servers"}
        user_choose = int(input("\n\033[33;1mplease enter your choose number:\033[0m").strip())

        while True:
            if user_choose in choose_dict.keys():
                print("\033[34;1m %s \033[0m".center(50, "*") % choose_dict[user_choose])
                for i, v in enumerate(d[choose_dict[user_choose]]):
                    print("\033[32;1m %s  %s \033[0m" % (i, v))
                break
            else:
                print("your enter has false，please try again!")
        return d

    @classmethod
    def read_config(cls):
        """
        通过 configparser 模块读取config.ini文件
        返回的数据格式为字典
        形如：
         {
         'web1': {'type': 'web_clusters', 'username': 'root', 'password': 'web11@@root', 'ip': '192.168.221.130', 'port': '22'},
         'web2': {'type': 'web_clusters', 'username': 'root', 'password': 'web2@@root', 'ip': '192.168.221.131', 'port': '11122'},
         'mysql1': {'type': 'db_servers', 'username': 'root', 'password': 'mysql1@@root', 'ip': '192.168.221.132', 'port': '11133'},
         'mysql2': {'type': 'db_servers', 'username': 'root', 'password': 'mysql2@@root', 'ip': '192.168.221.133', 'port': '11144'}
         }
        """
        # 实例化出一个配置解析器对象
        config = configparser.ConfigParser()
        config.read(config_file)
        # 将读取到的数据转化为字典的格式
        dict1 = dict(config._sections)
        # print("line 74:", d)
        for k in dict1:
            dict1[k] = dict(dict1[k])
        # print("line 80:", dict1)

        # hosts_list = config.sections()
        # print("line 72:", dict(hosts_list))
        # print("line 69:", hosts_list)
        # # web_clusters
        # # web = hosts_list[i]
        # username = config[hosts_list[0]]['username']
        # password = config[hosts_list[0]]['password']
        # ip = config[hosts_list[0]]['ip']
        # port = config[hosts_list[0]]['port']
        # print(config[hosts_list[0]]['type'])
        #
        # for i in range(len(hosts_list)):
        #     temp_list = []
        #     username = config[hosts_list[i]]['username']
        #     password = config[hosts_list[i]]['password']
        #     ip = config[hosts_list[i]]['ip']
        #     port = config[hosts_list[i]]['port']
        #     host_table[hosts_list[i]] = [username, password, ip, port]
        #
        #     # print(config[hosts_list[i]]['type'])
        #     if config[hosts_list[i]]['type'] in host_groups.keys():
        #         # username = config[hosts_list[i]]['username']
        #         # password = config[hosts_list[i]]['password']
        #         # ip = config[hosts_list[i]]['ip']
        #         # port = config[hosts_list[i]]['port']
        #         host_table[hosts_list[i]] = [username, password, ip, port]
        #         host_groups[config[hosts_list[i]]['type']] = host_table
        #
        #
        #         # print(host_groups[config[hosts_list[i]]['type']])
        #         host_groups[config[hosts_list[i]]['type']].append(hosts_list[i])
        #         # print('line 36:', host_groups[config[hosts_list[i]]['type']])
        #     else:
        #         host_groups[config[hosts_list[i]]['type']] = [hosts_list[i], ]
        #     # print(host_groups)
        # print(host_groups)
        return dict1

    @classmethod
    def welcome(cls):
        str1 = "\033[31;1m 欢迎来到主机管理系统! \033[0m"
        print(str1.center(50, "="))


if __name__ == "__main__":
    hm1 = HostManager()
    # hm1.read_config()
    HostManager.read_config()
