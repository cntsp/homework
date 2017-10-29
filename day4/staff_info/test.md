### 查询功能测试
请输入sql语句：select name,age from staff_table where age > 24
检测到select语句
{'18339063132': {'name': 'cntsp', 'age': '28'}, '18339063131': {'name': 'cheche', 'age': '25'}}
查询到2条数据。

请输入sql语句：select * from staff_table where dept = "manager"
检测到select语句
{'18339063131': {'age': '25', 'staff_id': '2', 'dept': 'manager', 'enroll_date': '2016-11-01', 'name': 'cheche'}}
查询到1条数据。
### 插入新员工功能测试
请输入sql语句：insert into staff_table (name,age,phone,dept,enroll_date) values (cnhyy,30,18339063134,boss,2010-09-26)
检测到insert语句
staff_table [['1', 'hushaohua', '24', '18339063130', 'it', '2016-09-01'], ['2', 'cheche', '25', '18339063131', 'manager', '2016-11-01'], ['3', 'cntsp', '28', '18339063132', 'clerk', '2016-09-11'], ['4', 'cnhyy', '30', '18339063134', 'boss', '2010-09-26']]
新员工记录创建成功

### 更新员工功能测试
请输入sql语句：UPDATE staff_table SET dept= "CEO" where dept="it"
检测到update语句
staff_table [['1', 'hushaohua', '24', '18339063130', 'ceo', '2016-09-01'], ['2', 'cheche', '25', '18339063131', 'manager', '2016-11-01'], ['3', 'cntsp', '28', '18339063132', 'clerk', '2016-09-11'], ['4', 'cnhyy', '30', '18339063134', 'boss', '2010-09-26']]
员工信息更新成功！

### 删除员工记录功能测试
请输入sql语句：delete from staff_table where id = 3
检测到delete语句
[['1', 'hushaohua', '24', '18339063130', 'ceo', '2016-09-01'], ['2', 'cheche', '25', '18339063131', 'manager', '2016-11-01'], ['3', 'cntsp', '28', '18339063132', 'clerk', '2016-09-11'], ['4', 'cnhyy', '30', '18339063134', 'boss', '2010-09-26']]
staff_table [['1', 'hushaohua', '24', '18339063130', 'ceo', '2016-09-01'], ['2', 'cheche', '25', '18339063131', 'manager', '2016-11-01'], ['4', 'cnhyy', '30', '18339063134', 'boss', '2010-09-26']]
ID号：3 员工信息已被删除！ 



