#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time;

ticks=time.time();
print("当前时间戳为：",ticks);


localtime=time.localtime(time.time());
print("本地时间为：",localtime);


print("---获取格式化时间-----");
localt=time.asctime(time.localtime(time.time()));
print(localt);


print("------格式化日期----------");
print(time.strftime("%Y-%m-%d %I:%M:%S %U",time.localtime()));
