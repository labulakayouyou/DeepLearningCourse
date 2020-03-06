# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

name：Zhou Yanming
描述：利用Python完成一元二次方程的求解，要求程序输入任意的值后，程序能判断输出有解或无解，有解的话，输出的解为多少。
"""

a=int(input("请输入二次项系数a="))
b=int(input("请输入一次项系数b="))
c=int(input("请输入常数c="))
'''
判断一元二次方程是否有解：判别式  b的平方-4ac>0 =0有解   <0无解   **幂运算
'''
judge=b*b-4*a*c
if judge>0:
    print("该方程有两个不同的解！")
    x1=float((-b+judge**0.5)/2*a)
    x2=float((-b-judge**0.5)/2*a)
    print("方程的两个根分别为：x1=%f，x2=%f"%(x1,x2))
elif judge==0:
    print("该方程有两个相同的解！")
    x1=float((-b+judge**0.5)/2*a)
    x2=float((-b-judge**0.5)/2*a)
    print("方程的两个根分别为：x1=%f，x2=%f"%(x1,x2))  
else:
    print("该方程无解！")
