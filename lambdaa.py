#coding=utf-8
f=lambda x,y,z:x*y*z;
#print(f(2,3,4));

g=lambda x,y=1,z=2:x*y*z;
#print(g(1));



data=list(range(1,20,1));
import random
random.shuffle(data);
data.sort(key=lambda x:x);
print(data);
data.sort(key=lambda x:len(str(x)),reverse=True);
print(data);
sorted(
print(data);
