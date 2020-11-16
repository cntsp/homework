import os
import sys
import configparser
# import commands

config_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(config_path)

config_file = config_path + '\\' + "config.ini"


class HostManager(object):
    def __init__(self):
        # HostManager.welcome()
        # HostManager.first_menu()
        # HostManager.host_service_function()
        pass

    @classmethod
    def host_service_function(cls):
        function_dict = {0: "exec_shell", 1: "put_file", 2: "exit_system"}
        print(""" 输入执行命令和上传文件命令前一定要仔细阅读 readme.md
            0 执行命令
            1 上传文件
            2 退出系统
        """)
        user_choose1 = int(input("please enter your choose:").strip())
        command = input("\n\033[34;1m请输入命令：\033[0m").strip()
        c1 = commands.Cmd(command)
        # print(hasattr(function_dict, user_choose1))
        if hasattr(c1, function_dict[user_choose1]):
            func = getattr(c1, function_dict[user_choose1])
            func()
        else:
            print("您的输入有误，请再次输入！")


    @classmethod
    def first_menu(cls):
        choose_dict = {}
        menu_dict = HostManager.read_config()
        for i, v in enumerate(menu_dict.keys()):
            print("\033[32;1m %s  %s \033[0m" % (i, v))
            choose_dict[i] = v

        print(choose_dict)
        user_choose = int(input("\n\033[33;1mplease enter your choose number:\033[0m").strip())
        while True:
            if user_choose in choose_dict.keys():
                print("\033[34;1m %s \033[0m".center(50, "*") % choose_dict[user_choose])
                for i, v in enumerate(menu_dict[choose_dict[user_choose]]):
                    print("\033[32;1m %s  %s \033[0m" % (i, v))
                break
            else:
                print("your enter has false，please try again!")

    @classmethod
    def read_config(cls):
        """
        通过 configparser 模块读取config.ini文件
        返回的数据格式为字典
        形如：{‘web_clusters’: ['web1','web2'], 'db_servers': ['mysql1','mysql2']}
        {'web_clusters':{'web1':["root","nihaoma","IP","port"], 'web2':[]}}
        """
        host_groups = {}
        # 实例化出一个配置解析器对象
        config = configparser.ConfigParser()
        config.read(config_file)
        # 读取主机，返回列表格式的主机名
        hosts_list = config.sections()
        print("line 69:", hosts_list)
        print(config[hosts_list[0]]['type'])
        for i in range(len(hosts_list)):
            # print(config[hosts_list[i]]['type'])
            if config[hosts_list[i]]['type'] in host_groups.keys():
                # print(host_groups[config[hosts_list[i]]['type']])
                host_groups[config[hosts_list[i]]['type']].append(hosts_list[i])
                # print('line 36:', host_groups[config[hosts_list[i]]['type']])
            else:
                host_groups[config[hosts_list[i]]['type']] = [hosts_list[i], ]
            # print(host_groups)
        print(host_groups)
        return host_groups

    @classmethod
    def welcome(cls):
        str1 = "\033[31;1m 欢迎来到主机管理系统! \033[0m"
        print(str1.center(50, "="))


if __name__ == "__main__":
    # hm1 = HostManager()
    # hm1.read_config()
    HostManager.read_config()
