#coding=utf-8

class A:
    def __init__(self,v1=2,v2=3):
        self._v1=v1;
        self.__v2=v2;
        
    def setValue(self,v1,v2):
        self._v1=v1;
        self.__v2=v2;
    def show(self):
        print(self._v1);
        print(self.__v2);
a=A();
print(a._v1);
#a.show();
print(a._A__v2);
