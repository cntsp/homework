import os
import sys
import paramiko
import re
import multiprocessing

# batch_run -h web1, web2, mysql1 -cmd "df -h"
# batch_scp -g web_clusters,db_servers -action put -local test.py -remote /tmp
# batch_run -g web_clusters,db_servers -cmd "df -h"

class Cmd(object):
    def __init__(self, command):
        self.command = command

    def explain_command(self):
        results = {}
        if self.command.startswith("batch_run"):
            webs_cmd = re.sub('"', '', self.command.split('-cmd')[1])
            if self.command.search('-h'):
                # results.append('h')
                results['type'] = 'h'
                webs_string = self.command.split('-h')[1].split('-cmd')[0]
                if webs_string.search(','):
                    webs_list = webs_string.split(',')
                webs_list = webs_string
                # 执行shell命令 return 出去的是 {'type': 'h', 'cmd': webs_cmd, 'webs_host': webs_list}
                # h代表是各个主机，g代表主机组
                # cmd   是需要执行的shell命令
                # webs_host 是指需要执行命令的各个主机列表
                results['cmd'] = webs_cmd
                results['webs_host'] = webs_list
                # print(webs_cmd)
                # print(webs_list)
            elif self.command.search('-g'):
                results['type'] = 'g'
                # results.append('g')
                webs_groups_string = self.command.split('-g')[1].split('-cmd')[0]
                if webs_groups_string.search(','):
                    webs_groups_list = webs_groups_string.split(',')
                else:
                    webs_groups_list = webs_groups_string
                # 执行shell命令 return 出去的是 {'type': 'h', 'cmd': webs_cmd, 'webs_groups': webs_groups_list}
                results['cmd'] = webs_cmd
                # results.append(webs_cmd)
                results['webs_groups'] = webs_groups_list

        elif self.command.startwith("batch_scp"):
            # batch_scp -h we1,web2 -action put -local test.py -remote /tmp/
            # batch_scp -g web_clusters,db_servers -action put -local test.py -remote /tmp

            # 解析出源文件
            source_file = self.command.split('-local')[1].split('-remote')[0]
            # 解析出目的目录
            destination_directory = self.command.split('-remote')[1]
            results['source_file'] = source_file.strip()
            results['destination_directory'] = destination_directory

            if self.command.search("-h"):
                webs_string = self.command.split('-h')[1].split('-action')[0]
                if webs_string.search(','):
                    webs_list = webs_string.split(',')
                else:
                    webs_list = webs_string
                # 执行shell命令 return 出去的是 {'type': 'h', 'cmd': webs_cmd, 'webs_groups': webs_list}
                results['webs_host'] = webs_list

            elif self.command.search("-g"):
                webs_string = self.command.split('-h')[1].split('-action')[0]
                if webs_string.search(','):
                    webs_groups_list = webs_string.split(',')
                else:
                    webs_groups_list = webs_string
                results['webs_groups'] = webs_groups_list

        else:
            print("你输入的命令有误!")

        return results

    def exec_shell(self):
        data_dict = self.explain_command()   # {'type': 'h', 'cmd': webs_cmd, 'webs_host': webs_list}
        if data_dict['type'] == "h":
            webs_host = data_dict['webs_host']
            for i in webs_host：

        host_information = {"web1": {"username":"root", "password": "nihaoma", "port":"22"}, "web2": {}}
        for i in
        p1 = multiprocessing.Process(target=self.exec_run, args=())
        self.exec_run(data_dict)


    @classmethod
    def exec_run(cls, data_dict):
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在 know_hosts 文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


        print("in the exec_shell")

    def put_file(self):
        data_dict = self.explain_command()
        print("in the put_file", self.command)

    def exec_system(self):
        exit()

