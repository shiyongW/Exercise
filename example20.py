#coding=utf-8

import random

def demo(lit):
    m=min(lit);
    print("mmmmmm,",m);
    result=(m,);
    #print(result);
    pos=[index for index,value in enumerate(lit)if value==m];
    #print(pos);
    result=result+tuple(pos);
    return result;
x=[random.randint(1,20) for i in range(100)];
print(x);
print(demo(x));
