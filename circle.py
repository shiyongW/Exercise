#coding=utf-8
from math import pi as PI
def CircleArea(r):
    if isinstance(r,(int,float)):
        return PI*r*r;
    else:
        print('you must give me an integer or float as radius');

print(CircleArea(11));


#返回平均数及大于平均数
def demo(*p):
    avg=sum(p)/len(p);
    g=[i for i in p if i>avg];
    return (avg,)+tuple(g);
print(demo(1,2,3,4))

#接收字符串参数，返回一个元组，其中第一个元素为大写字母的个数，第二个元素为小写字母的个数
def demoo(s):
    result=[0,0];
    for ch in s:
        if 'a'<=ch<='z':
            result[1]+=1;
        elif 'A'<=ch<='Z':
            result[0]+=1;
    return result;
print(demoo('aaaaaSDFSDFSDFbbddddddddssfsdfsdfdddbdLKSJDFSDF'));
