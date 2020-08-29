__Author__ = "CNTSP"

import os, sys, re
# 为了导入另一个目录下的模块，需要增加环境变量的搜索路径
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# list.insert(index, obj)  index --对象obj需要插入的索引位置  obj--要插入列表中的对象元素
# sys.path 是python的模块的搜索路径，是一个 列表格式的 对象
sys.path.insert(0, base_dir)


from modules import calc

if __name__ == "__main__":
    flag = False
    while not flag:
        expression = input("请你输入四则运算表达式 或【按q键退出】 \n >>>")
        # 去掉表达式中所有的空格
        expression_input = expression.replace(" ",'')
        if expression_input == 'q':
            flag = True
        elif re.search('[A-Za-z]+', expression_input):
            print("四则运算式中不要包含大小字母！")
        else:
            #print(exp_input)
            print("################################")
            print('正则解析表达式 %s 计算结果：%s' %(expression_input, calc.core(expression_input)))
            print("使用 eval 工具 计算出的结果为：%s" %eval(expression_input))