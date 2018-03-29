#coding=utf-8
#2 elif 用法
num=int(input('Please input your number:'));
if num==3:
    print('boss,',num);
elif num==2:
    print('user,',num);
elif num==1:
    print('worker,',num);
elif num<0:
    print('error,',num);
else:
    print('roadman,',num);
    
