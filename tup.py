#coding=utf-8
#!/usr/bin/python
tup1=('Jim','Tom','Johannes',123,567);
tup2=(1,2,3,4,5,6,7,8);
tup3="a","b","c","d";
print ("tup1[1:3]=",tup1[1:3]);
tup4=tup2+tup3;
print (tup4);
print (len(tup4));# length
print('----------------------------------');
print(tup2*3);#复制
print('a' in tup3);# judge someone in tup
for x in tup1:
    print(x);
print('----------------------------------');
print(tup1[2]);
print(tup1[2:]);
print(tup1[:-2]);
