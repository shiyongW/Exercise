#!/usr/bin/python
# -*- coding:UTF-8 -*-

#导入pandas、numpy、matplotlib、operator包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator

#读取文件
df = pd.read_table('zhong.txt',header=None,sep=',')

#截取日期
tdate = sorted(df.loc[:,0])

#截取红球，2个红球组合方式
h1 = df.loc[:,1:2].values
# print h1
h2 = df.loc[:,2:3].values
h3 = df.loc[:,3:4].values
h4 = df.loc[:,4:5].values
h5 = df.loc[:,5:6].values

# b1 = df.loc[:,7:7].values
# print b1

h6 = df.loc[:,1:3:2].values

h7 = df.loc[:,1:4:3].values
h8 = df.loc[:,1:5:4].values
h9 = df.loc[:,1:6:5].values

h10 = df.loc[:,2:4:2].values
h11 = df.loc[:,2:5:3].values
h12 = df.loc[:,2:6:4].values

h13 = df.loc[:,3:5:2].values
h14 = df.loc[:,3:6:3].values

h15 = df.loc[:,4:6:2].values

# data2 = np.append(h1, b1, axis=1)

#将截取的2个红球，组合到一起
data2 = h1
for i in [h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15]:
    data2 = np.append(data2, i, axis=0)
print(len(data2))

#数据放到DataFrame
data1 = pd.DataFrame(data2)
# print data1

#输出数据到文件
data1.to_csv('2hdata.csv',index=None,header=None)

#以字典方式将数据进行统计，并从大倒小排序
f = open("2hdata.csv")
count_dict = {}
for line in f.readlines():
    line = line.strip()
    count = count_dict.setdefault(line, 0)
    count += 1
    count_dict[line] = count
sorted_count_dict = sorted(count_dict.items(), key=operator.itemgetter(1), reverse=True)
# for item in sorted_count_dict:
#     print "%s,%d" % (item[0], item[1])

# print sorted_count_dict

#重置DataFrame的index  
fenzu = pd.DataFrame(sorted_count_dict).set_index([0])
print(fenzu)

x = list(fenzu.index[:19])
y = list(fenzu.values[:19])
print(x)
print(y)

#将index替换成数值，便于画图使用  
s = pd.Series(range(1,len(x)+1), index=x)

#设置画图的属性
plt.figure(figsize=(12,8),dpi=80)
plt.legend(loc='best')

plt.bar(s,y,alpha=.5, color='r',width=0.8)
plt.title('The two red ball number')
plt.xlabel('two red number')
plt.ylabel('times')
# for i in  range(0,19):
#     plt.text(int(i+1.4),25,x[i],color='b',size=10)
# plt.text(1.4,20,x[0],color='g',ha='center')
#将原来index的内容显示出来  
plt.xticks(s,x, rotation=30,size=10,ha='left')
plt.show()
