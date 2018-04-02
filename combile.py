#coding=utf-8
dd=(1,2,3,4,5,6,7);
for i in dd:
    ii=i*100;
    for j in dd:
         if i==j:
             continue;
         jj=j*10;
         for k in dd:
            if k==i or k==j:
                continue;
            print(ii+jj+k,end=' ');
