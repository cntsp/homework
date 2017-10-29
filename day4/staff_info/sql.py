__Author__ = "CNTSP"

import re,json
import configparser
primary_key = ''
auto_increment = ''
key_index = ''

def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    global primary_key
    global auto_increment
    global key_index
    primary_key = config['db_config']['primary_key']
    auto_increment = config['db_config']['auto_increment']
    key_index = json.loads(config['db_config']['key_index'])

def get_data(table,keys,limit):
    '''
    获取数据
    :param table: 表名/文件名
    :param keys:  字段
    :param limit:  限制条件
    :return:
    '''
    temp_data = get_table_data(table)
    limit_list = limit_parse(limit)
    a = limit_data(temp_data,keys,limit_list)
    print(a)
    print('查询到%d条数据。'%(len(a)))

def get_table_data(table):
    temp_data = []
    with open('%s.txt' %(table),'r',encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            temp_data.append(line.split(','))
    #print(temp_data)
    return temp_data

def limit_parse(limit):
    limit_keys = ['>','<','=','like']
    limit = limit.replace(' ','')
    for key in limit_keys:
        if key in limit:
            res = limit.split(key)
            res[1]= res[1].strip('"')
            res.append(key)
    #print(res) # ['age', 22, '>'] ['dept','it','=']
    return res

def limit_data(temp_data,keys,limit):
    """
    解析限制条件函数
    :param temp_data: 每个员工信息存放在列表中
    :param keys:  查询关键字段
    :param limit:  查询条件
    :return:
    """
    res_data = {}
    key_list = []
    if '*' in keys:
        for key in key_index:
            key_list.append(key)
    else:
        key_list = keys.split(',') #[name,age]
    #print("temp_data:%s" %temp_data)
    for item in temp_data:
        res_data[item[key_index[primary_key]]] = {}
        #print(key_index)
        #print("item:%s" %item)  ['1', 'Alex Li', '22', '18339063130', 'it', '2016-09-01']
        for index in key_index:
            #print("index:%s" %index)
            if primary_key != index and index in key_list:
                res_data[item[key_index[primary_key]]][index] = item[key_index[index]]# res_data['18339063130']['age'] = 22
    #print("res_data:%s limit:%s" %(res_data,limit))  # res_data:{'18339063130': {'age': '22', 'name': 'Alex Li'}, '18339063138': {'age': '27', 'name': 'cntsp'}, '18339063131': {'age': '25', 'name': 'cheche'}} limit:['age', '23', '>']
    return final_data(res_data,limit)

def final_data(temp_data,limit):
    res_data = {}
    if limit[2] == '=':
        for item in temp_data:
            if temp_data[item][limit[0]].lower() == str(limit[1]):
                res_data[item] = temp_data[item]
    elif limit[2] == '<':
        for item in temp_data:
            if temp_data[item][limit[0]] < str(limit[1]):
                res_data[item] = temp_data[item]
    elif limit[2] == '>':
        for item in temp_data:
            #print("\033[31;1mitem:%s\033[0m" %item) 18339063130
            if temp_data[item][limit[0]] > str(limit[1]):
                res_data[item] = temp_data[item]
    elif limit[2] == 'like':
        for item in temp_data:
            if str(limit[1]) in temp_data[item][limit[0]].lower():
                res_data[item] = temp_data[item]
    return res_data

def sql_search(sql):
    res = re.search(r'select\s+((\w+,)*(\w+)?)?(\*)?\s+from\s+\w+',sql)
    if res is None:
        print('\033[31;1msearch 语法错误!\033[0m')
    else:
        keys_table = res.group()
        #print(keys_table)
        keys = keys_table.replace('select','')
        keys = keys.split('from')
        table = keys[1].strip()
        keys = keys[0].strip()
        limit = sql.split(res.group())[-1].replace('where','').strip()
        #print("keys:%s table:%s limit:%s"%(keys,table,limit))
        get_data(table, keys, limit)

def sql_insert(sql):
    res = re.search(r'insert\s+into\s+(\w+)\s+\((\w+,){4}(\w+)\)\s+values\s+',sql)
    if res is None:
        print("\033[31;1minsert 语法错误！\033[0m")
    else:
        #print("res.group:%s" %res.group())
        table_name = res.group(1)
        #print("res.group(1):%s" %res.group(1))
        field_name_group = res.group(2)
        #print("res.group(2):%s" %res.group(2))
        filed_value_group = sql.split(res.group())[-1].rstrip(')').lstrip('(').split(',')
        temp_data = get_table_data(table_name)
        #print(temp_data)
        filed_value_group.insert(0,str(len(temp_data)+1))
        #print(temp_data,len(temp_data))
        temp_data.append(filed_value_group)
        insert_state = write_data(table_name, temp_data)
        if insert_state:
            print("\033[31;1m新员工记录创建成功\033[0m")

def sql_delete(sql):
    res = re.search(r'delete\s+from\s+(\w+)\s+where\s+',sql)
    if res is None:
        print("\033[31;1mdelete 语法错误\033[0m")
    else:
        table_name = res.group(1)
        limit_id_number = sql.split(res.group())[-1].split(' ')[-1]
        delete_data(table_name, limit_id_number)

def sql_update(sql):
    res = re.search(r'update\s+(\w+)?\s+set\s+(\w+)\s{0,5}=\s{0,5}"(\w+)"\s+where\s+(\w+)\s{0,5}=\s{0,5}"(\w+)"',sql)
    if res is None:
        print("\033[31;1mdelete 语法错误\033[0m")
    else:
        table_name = res.group(1)
        modify_filed = res.group(2)
        modify_value = res.group(3)
        old_value = res.group(5)
        #print(table_name,modify_filed,modify_value)
        temp_data = get_table_data(table_name)
        #print(key_index)
        num = 0
        if modify_filed in key_index.keys():
            for line in temp_data:
                if old_value in line:
                    temp_data[num][key_index[modify_filed]] = modify_value
            num +=1
        #print(temp_data)
        update_state = write_data(table_name,temp_data)
        if update_state:
            print("\033[31;1m员工信息更新成功！\033[0m")

def check_sql(sql):
    sql = sql.strip().lower()
    if sql.startswith('select'):
        print("\033[32;1m检测到select语句\033[0m")
        sql_search(sql)
    elif sql.startswith('insert'):
        print("\033[32;1m检测到insert语句\033[0m")
        sql_insert(sql)
    elif sql.startswith('delete'):
        print("\033[32;1m检测到delete语句\033[0m")
        sql_delete(sql)
    elif sql.startswith('update'):
        print("\033[32;1m检测到update语句\033[0m")
        sql_update(sql)
    else:
        print("\033[31;1m您输入的不符合SQL语法！\033[0m")


def delete_data(table_name, id_number):
    """
    输入指定id的员工记录
    :param table_name: 表名
    :param id_number:  员工id
    :return:
    """
    temp_data = get_table_data(table_name)
    print(temp_data)
    for i in temp_data:
        if i[0] == id_number:
            del temp_data[int(id_number) - 1]
    write_data(table_name, temp_data)
    print("\033[31;1mID号：%s 员工信息已被删除！ \033[0m" % id_number)

def write_data(table_name,table_temp_data):
    """
    写入新数据
    :param table_name: 表名
    :param table_temp_data: 临时字段信息
    :return:
    """
    print(table_name, table_temp_data)
    with open("%s.txt" %table_name, 'w',encoding="utf-8") as f1:
        for i in table_temp_data:
            line = ','.join(i)
            f1.write("%s\n" %line)
    return True

if  __name__ == '__main__':
    sql = input('请输入sql语句：')
    get_config()
    check_sql(sql)