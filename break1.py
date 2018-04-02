#coding=utf-8
for i in range(100,1,-1):
    for n in range(2,i,1):
        if i%n==0:
            break;
    else:
        print(i,end='   ');
       # break;
