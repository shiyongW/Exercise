#coding=utf-8

for i in range(1,10,1):
    for j in range(1,i+1,1):
        print('{0}*{1}={2}'.format(i,j,i*j),end=' ');
    else:
        print();


for i in range(200,1,-1):
    if(i%17==0):
        print(i);
        break;
