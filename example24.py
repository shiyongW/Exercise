#coding=utf-8

# 模拟发红包

import random

def hongbao(total,num):
    #total 发送红包总金额
    #num 发送红包总数量
    each=[];
    # 已发送红包总金额
    already=0;
    for i in range(1,num):
        t=random.randint(1,(total-already)-(num-i));
       # print("tttt=",t);
        each.append(t);
        already=already+t;
        #剩余的钱发给最后一个人
    each.append(total-already);
    return each;

if __name__=='__main__':
    total=200;
    num=100;
    for i in range(3):#模拟次数
        each=hongbao(total,num);
        print(each);
