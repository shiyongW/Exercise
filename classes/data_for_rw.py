#coding=utf-8

class Test:
    def __init__(self,value):
        self.__value=value;

    def __get(self): #读取私有数据成员的值
        return self.__value;
    def __set(self,v):#修改私有数据成员的值
        self.__value=v;

    def __del(self):
        del self.__value;

    value=property(__get,__set,__del);#可读 可写属性，指定相应的读写方法
    def show(self):
        print(self.__value);

t=Test(5);
print(t.value);

t.value=30;
t.show();


del t.value;
print(t.value);
