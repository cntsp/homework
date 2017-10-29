# 第四周作业  员工信息表程序-实现增删改查操作

### 作者介绍
 * Author: cntsp
 * My Blog: [https://cntsp.github.io](https://cntsp.github.io)
 
### 功能实现
> * 可进行模糊查询，语法至少支持下面3种:
select name,age from staff_table where age > 22
select  * from staff_table where dept = "IT"
select  * from staff_table where enroll_date like "2013"
> * 查到的信息，打印后，最后面还要显示查到的条数
> * 可创建新员工纪录，以phone做唯一键，staff_id需自增
> * 可删除指定员工信息纪录，输入员工id，即可删除
> * 可修改员工信息，语法如下:
　　UPDATE staff_table SET dept="Market" where dept = "IT"
 
### 环境依赖
> * Pycharm(python3.4)

### 目录结构
> * config.ini : 全局配置文件
> * sql.py : 主程序
> * staff_table.txt : 员工信息文件

### staff_table.txt该文件初始只有3条员工信息如下：
1,hushaohua,24,18339063130,it,2016-09-01
2,cheche,25,18339063131,manager,2016-11-01
3,cntsp,28,18339063132,clerk,2016-09-11


