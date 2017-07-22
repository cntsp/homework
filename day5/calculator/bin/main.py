__Author__ = "CNTSP"

import os, sys, re
# 为了导入另一个目录下的模块，需要增加环境变量的搜索路径
a = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# list.insert(index, obj)  index --对象obj需要插入的索引位置  obj--要插入列表中的对象元素
sys.path.insert(0,a)
#print(sys.path)

from modules import calc

if __name__ == "__main__":
    flag = False
    while not flag:
        expression = input("请你输入四则运算表达式 或【q键=退出】 \n >>>")
        # 去掉表达式中所有的空格
        exp_input = expression.replace(" ",'')
        if exp_input == 'q':
            flag = True
        elif re.search('[A-Za-z]+',exp_input):
            print("四则运算式中不要包含大小字母！")
        else:
            #print(exp_input)
            print("################################")
            print('表达式 %s 计算结果：%s' %(exp_input,calc.core(exp_input)))
            print("eval 计算出的结果为：%s" %eval(exp_input))