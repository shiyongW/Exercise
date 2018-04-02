#coding=utf-8
def compr(n):
    '''数值比较'''
    a,b=1,1;
    while a<n:
        print(a,end=' ');
        a,b=b,a+b;

    print();
        
#compr(6);

def demo(a,b,c=5):
    ''''关键参数'''
    print(a,b,c);


#demo(3,7);
#demo(b=3,c=1,a=9);

def demo1(*p):
    '''元组'''
    print(p);
#demo1(1,2,3,4,5,6,7,322);

def demo2(**p):
    '''字典'''
    for i in p.items():
        print(i);

#demo2(x=1,y=4,z=5,u=2);


# 传递参数时的序列解包
def mm(a,b,c):
    print(a+b+c);

seq=[34,32,1];
#mm(*seq);

dic={1:'a',2:'b',3:'c'};
#mm(*dic);
set={1,2,3};
#mm(*set);
#mm(*dic.values());

demo(1,*(2,3));
demo(*(2,3),c=3)

