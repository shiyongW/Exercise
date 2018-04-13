#coding=utf-8

class Root:
    __total=0;
    
    def __init__(self,v):
        self.__value=v;
        Root.__total+=1;

    def show(self):  #实例方法  self 表示 类对象自身
        print("self.__value=",self.__value);
        print("Root.__total=",Root.__total);

    @classmethod  #修饰器，声明类方法
    def classShowTotal(cls):  #类方法  cls 表示 类 自身
        print(cls.__total);

    @staticmethod #修饰器，声明静态方法
    def staticShowTotal():#静态方法
        print(Root.__total);


r=Root(2);
r.classShowTotal();  #通过对象调用类方法

r.staticShowTotal(); #通过对象调用静态方法

r.show();# 通过对象调用实例化方法
r=Root(3);
Root.classShowTotal(); #通过类名调用类方法

Root.staticShowTotal();#通过类名调用静态方法

#Root.show();# 通过类名不能调用对象的实例化方法  公有方法或私有方法

Root.show(r); # 可以调用实例化的成员
    
