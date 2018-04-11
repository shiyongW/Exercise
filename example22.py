#coding=utf-8
# 偶数，输出两个素数，且素数之和等于偶数
import math

def isPrime(n):
    m=int(math.sqrt(n))+1;
    for i in range(2,m):
        if n%i==0:
            return False;
        else:
            return True;

def demo(n):
    if isinstance(n,int) and n>0 and n%2==0:
        for i in range(3,int(n/2)+1):
            if(i%2==1 and isPrime(i) and isPrime(n-i)):
                print(i,'+',n-i,'=',n);


demo(67);
