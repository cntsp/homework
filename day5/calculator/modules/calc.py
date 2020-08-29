__Author__ = "CNTSP"

import re

def delete(f_list,f_index):
    """
    删除列表元素
    :param f_list: 输入列表
    :param f_index: 输入要删除的运算符的位置
    :return:
    """
    # 列表的删除有先后顺序
    del f_list[f_index+1]
    del f_list[f_index]
    del f_list[f_index-1]
    return f_list

def add(f_list):
    """
    加法计算
    :param f_list:
    :return:
    """
    result = 0
    for i in f_list:
        result += float(i)
    return str(result)
def minus(subtraction1,subtraction2):
    """
    减法计算
    :param subtraction1:
    :param subtraction2:
    :return:
    """
    result = 0
    result = float(subtraction1) - float(subtraction2)
    return str(result)

def divide(divisor,divide1):
    """
    除法计算
    :param divisor:
    :param Divide:
    :return:
    """
    result = 0
    result = float(divisor)/float(divide1)
    return str(result)

def multiply(mult1,mult2):
    """
    乘法计算
    :param mult1:
    :param mult2:
    :return:
    """
    result = 0
    result = float(mult1) * float(mult2)
    return str(result)

def calculation(f_list):
    """
    计算分解后的表达式
    :param f_list: 输入列表
    :return:
    """
    print(f_list)
    flag = False
    while not flag:
        if f_list.count('/'):
            f_index = f_list.index('/')
            divide_result = divide(f_list[f_index-1], f_list[f_index+1])
            f_list = delete(f_list, f_index)
            f_list.insert(f_index-1, str(divide_result))
        elif f_list.count('*'):
            f_index = f_list.index('*')
            multiply_result = multiply(f_list[f_index-1], f_list[f_index+1])
            f_list = delete(f_list, f_index)
            f_list.insert(f_index-1, str(multiply_result))
        elif f_list.count('-'):
            f_index = f_list.index('-')
            minus_result = minus(f_list[f_index-1], f_list[f_index+1])
            f_list = delete(f_list, f_index)
            f_list.insert(f_index-1, str(minus_result))
        else:
            if f_list.count('+'):
                f_index = f_list.index('+')
                del f_list[f_index]
            sum_add = add(f_list)
            flag = True
    return sum_add

def formula_to_list(formula):
    """
    将括号内的计算式形如：(24+14*15)转换成列表：[24,'+14','*',15]
    :param formula:  输入计算式
    :return: 返回列表
    """
    # 判断是否是包含括号的表达式项
    if re.findall('\(.+\)', formula):
        formula = formula[1:-1]  # 利用切片去掉括号
        print(formula)
    f_list = []
    for i in formula:
        if len(f_list)==0:
            f_list.append(i)
        elif i in '+-*/':
            f_list.append(i)
        else:
            if f_list[-1] in '*/':
                f_list.append(i)
            else:
                f_list[-1] += i
    # print(f_list)
    return f_list

def core(formula):
    """
    括号计算判断
    :param formula:
    :return:
    """
    # re.search(pattern,string,flags=0) 匹配到返回一个_sre.SRE_Match对象，匹配不到返回None
    # r'\([^()]+)\' 对这个匹配 pattern 理解：匹配无嵌套小括号的小括号，并且返回第一个匹配到的对象
    if re.search(r'\([^()]+\)', formula):

        # match.group(0) match是re.search(r'\([^()]+\)',formula)返回的match object,组0表示整个匹配到字串
        # braces_contents: 第一次匹配到的小括号表达式内容

        braces_contents = re.search(r'\([^()]+\)', formula).group(0)
        print("braces_contents is %s " % braces_contents)

        result = calculation(formula_to_list(braces_contents))
        # sub(pattern, repl, string, count=0, flags=0)
        formula = re.sub(r'\([^()]+\)', result, formula, count=1) # 1表示替换第一个匹配到的字串
        return core(formula)
    else:
        return calculation(formula_to_list(formula))



