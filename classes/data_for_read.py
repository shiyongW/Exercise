#coding=utf-8

class Test:
    def __init__(self,v):
        self.__value=v;
    @property  #修饰器，定义属性，提供对私有数据成员的访问
    def showData(self):
        return self.__value;


t=Test(5);
print(t.showData);
t.value=3;
print(t.value);
