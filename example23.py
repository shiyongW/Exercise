#coding=utf-8
#最大公约数 最小公倍数


def demo(m,n):
    if(m>n):
        m,n=n,m;
    p=m*n;
    while(m!=0):
        r=n%m;
        n=m;
        m=r;
    return (n,int(p/n));

print(demo(20,30));

import math
def dem1(m,n):
    r=math.gcd(m,n);# 计算最大公约数
    print(r,int(m*n/r));

dem1(45,10);
dem1(34,17)
