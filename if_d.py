#coding=utf-8
num=int(input('please input your number:'));
if num>=0 and num<=10:
    print('>=0 and <=10',num);

if num<0 or num>10:
    print('<0 or >10',num);
else:
    print('undefined',num);

if(num>=0 and num<=5) or (num>=10 and num<=15):
    print('hello');
else:
    print('underfine.');

if num==100:
    print("变量num的值为:",num);

print("Good bye!");
