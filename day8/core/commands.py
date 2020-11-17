import os
import sys
import paramiko
import re
import multiprocessing
import main

# batch_run -h web1, web2, mysql1 -cmd "df -h"
# batch_scp -g web_clusters,db_servers -action put -local test.py -remote /tmp
# batch_run -g web_clusters,db_servers -cmd "df -h"

class Cmd(object):
    def __init__(self, command, d):
        self.command = command
        self.d = d

    def explain_command(self):
        results = {}
        if self.command.startswith("batch_run"):
            webs_cmd = re.sub('"', '', self.command.split('-cmd')[1])
            print('line 20:', webs_cmd)
            if re.search(' -h ', self.command):
                # results.append('h')
                results['type'] = 'h'
                webs_string = self.command.split('-h')[1].split('-cmd')[0]
                if re.search(',', webs_string):
                    # print("line 26:", webs_string)
                    webs_string = webs_string.split(',')
                    print('line 28', webs_string)
                webs_list = webs_string
                # 执行shell命令 return 出去的是 {'type': 'h', 'cmd': webs_cmd, 'webs_host': webs_list}
                # h代表是各个主机，g代表主机组
                # cmd   是需要执行的shell命令
                # webs_host 是指需要执行命令的各个主机列表
                results['cmd'] = webs_cmd
                results['webs_host'] = webs_list
                # print(webs_cmd)
                # print(webs_list)
                print("##################################")
            elif re.search(' -g ', self.command):
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                results['type'] = 'h'
                # results.append('g')
                webs_groups_string = self.command.split('-g')[1].split('-cmd')[0]
                print("line 42", webs_groups_string)
                print("line 43", self.d)
                if re.search(',', webs_groups_string):
                    webs_groups_list = webs_groups_string.split(',')
                else:
                    webs_groups_list = webs_groups_string
                # 执行shell命令 return 出去的是 {'type': 'h', 'cmd': webs_cmd, 'webs_groups': webs_groups_list}
                results['cmd'] = webs_cmd
                # results.append(webs_cmd)
                if isinstance(webs_groups_string, str):
                    print("line 55:", webs_groups_string)
                    webs_groups_string = webs_groups_string.strip()
                    results['webs_host'] = self.d[webs_groups_string]
                elif isinstance(webs_groups_string, list):
                    for i in webs_groups_string:
                        results['webs_host'].append(self.d[i])

        elif self.command.startswith("batch_scp"):
            # batch_scp -h we1,web2 -action put -local test.py -remote /tmp/
            # batch_scp -g web_clusters,db_servers -action put -local test.py -remote /tmp

            # 解析出源文件
            source_file = self.command.split('-local')[1].split('-remote')[0]
            # 解析出目的目录
            destination_directory = self.command.split('-remote')[1]
            results['source_file'] = source_file.strip()
            results['destination_directory'] = destination_directory

            if re.search("-h", self.command):
                webs_string = self.command.split('-h')[1].split('-action')[0]
                if re.search(',', webs_string):
                    webs_list = webs_string.split(',')
                else:
                    webs_list = [webs_string.strip()]
                # 执行shell命令 return 出去的是 {'type': 'h', 'cmd': webs_cmd, 'webs_groups': webs_list}
                results['webs_host'] = webs_list

            elif re.search("-g", self.command):
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
        # 读取配置文件，获取SSH客户端所需的信息
        data_dict1 = main.HostManager.read_config()
        data_dict2 = self.explain_command()   # {'type': 'h', 'cmd': webs_cmd, 'webs_host': webs_list}
        pro = []
        print("line 87", data_dict1)
        print("line 88:", data_dict2)
        if data_dict2['type'] == "h":
            print("in the commands module: line 90")
            webs_host = data_dict2['webs_host']
            print(" line 92:", webs_host)
            print(isinstance(webs_host, str))
            if isinstance(webs_host, str):
                print("line 95")
                webs_host = webs_host.strip()
                if webs_host in data_dict1.keys():
                    # {'type': 'web_clusters', 'username': 'root', 'password': 'web11@@root', 'ip': '192.168.221.130', 'port': '22'}
                    p1 = multiprocessing.Process(target=self.exec_run, args=(webs_host, data_dict2['cmd'], data_dict1[webs_host]))
                    p1.start()
                    pro.append(p1)
                for j in pro:
                    j.join()
            if isinstance(webs_host, list):
                print("@@@line 105:", webs_host)
                for j in webs_host:
                    j = j.strip()
                    if j in data_dict1.keys():
                        # {'type': 'web_clusters', 'username': 'root', 'password': 'web11@@root', 'ip': '192.168.221.130', 'port': '22'}
                        p1 = multiprocessing.Process(target=self.exec_run, args=(j, data_dict2['cmd'], data_dict1[j]))
                        p1.start()
                        pro.append(p1)
                for j in pro:
                    j.join()
        else:
            pass
    @classmethod
    def exec_run(cls, hostname, order, data_dict):
        """
        hostname: 主机名
        order: 执行的命令
        data_dict: 主机的
        """
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在 know_hosts 文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=data_dict["ip"], port=data_dict["port"], username=data_dict["username"], password=data_dict["password"])
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(order)
        # 获取命令结果
        result = stdout.read()
        # result = stdout if ssh.exec_command(order).read() else stdin
        output = "\033[31;1m %s 执行 %s 命令输出结果：\033[0m" % (hostname, order)
        print(output.center(70, "*"))
        print(result.decode())

    def put_file(self):
        # 读取配置文件，获取SSH客户端所需的信息
        data_dict1 = main.HostManager.read_config()
        print("line 155:", data_dict1)
        data_dict2 = self.explain_command()
        print("line 154:", data_dict2)
        print("in the put_file", self.command)
        webs_host = data_dict2['webs_host']
        for i in webs_host:
            if i in data_dict1.keys():
                p1 = multiprocessing.Process(target=self.put_run, args=(i, data_dict2, data_dict1))

    @classmethod
    def put_run(cls):
        pass


    def exit_system(self):
        exit()

