#!/usr/bin/python

dict={'name':'Johannes','age':32,'class':'Three'};

print("dict['name']:",dict['name']);

print("dict['class']:",dict['class']);

print('-----------update------------');
dict['age']=33;
dict['class']='Four';

print(dict);

print('-----------add------------');
dict['school']="山东工商学院";

st=str(dict['school']);
print("输出字典可打印的字符串标识",st);

print('-----------delete data------------');
del dict['age'];
print(dict);
print('-----------clear------------');
dict.clear();#清空词典所有条目
print(dict);
print('-----------delete------------');
del dict; #删除词典

print(dict);

