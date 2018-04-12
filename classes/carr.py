#coding=utf-8
#from types import MethodType
import types
class Car(object):
    price=1000;# 类的数据成员
    def __init__(self,c):
        self.color=c; #对象的数据成员

car1=Car("red");#实例化对象
car2=Car("Blue");
print(car1.color,Car.price);
Car.price=1100;
Car.name='QQ';#动态增加类的数据成员
car1.color="yellow";
print(car2.color,Car.price,Car.name);
print(car1.color,Car.price,Car.name);


def setSpeed(self,s):
    self.speed=s;

car1.setSpeed=types.MethodType(setSpeed,car1);#动态为对象增加成员方法
car1.setSpeed(30);#调用成员对象方法
print(car1.speed);
    
