# -*- coding: utf-8 -*-
"""
5-1 题目：

生成一个[0,1)之间均匀分布的随机数数组，包含1000个元素， 随机种子为612。
接收用户输入一个1-100之间的数字。打印随机数组中所有索引值可以被输入整数整
除的数字，并打印序号和索引值。序号从1
开始，依次加1.  例如，用户输入50，则
打印数组中索引值为0,50,100...1000的随机数。

请输入一个1-100之间的整数：50
序号   索引值   随机数
1 	   0   	   0.1434716297030787
2 	   50 	   0.3228752619106986
3 	   100 	   0.39412407684983874
......
20 	   950 	   0.4658222822786575

"""
import numpy.matlib
import numpy as np

zz01 = np.random.seed(612)
zz01 = np.random.uniform(0,1,1000)
i = 1
n = int(input('请输入一个1-100之间的整数：'))
print('序号\t索引值\t随机数')
for x in range(0, 1000, n):
    print(i, x, zz01[x], sep='\t')
    i = i + 1
     
    
 
"""
for x in ...循环    把每个元素代入变量x
range(0,0,M)意思是从列表的下标为0的元素开始，以M为间隔，一直取到下标为1000的元素（但是不包括下标为1000元素）
print(zz01.ndim)     打印zz01数组的维数
print(zz01.shape)    打印zz01数组的形状
print(zz01.size)     打印zz01数组的元素总个数
print(zz01.dtype)    打印zz01数组的元素数据类型
"""
