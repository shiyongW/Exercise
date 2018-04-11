#coding=utf-8
import random
secret=random.randint(1,10);
temp=input("猜猜我心里想的什么数:");
guess=int(temp);
while(guess!=secret):
    temp=input("猜错了，再猜猜~");
    guess=int(temp);
    if guess==secret:
        print("恭喜你~猜中了！！！！");
    elif guess>secret:
        print("猜大了~");
    else:
        print("猜小了~");
print("不玩了~");
