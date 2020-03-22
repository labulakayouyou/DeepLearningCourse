# -*- coding: utf-8 -*-

x = [64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
y = [62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]

sumX = 0
sumY = 0
formula1 = 0
formula2 = 0

for i in range(len(x)):
    sumX += x[i]
    
AVGx = sumX / len(x)


for j in range(len(y)):
    sumY / len(y)
    
AVGy = sumY / len(y)


for i in range(10):
    formula1 += (x[i] - AVGx) * (y[i] - AVGy)
    formula2 += (x[i] - AVGx) * (x[i] - AVGx)
    
w = formula1/ formula2
print("W的值为：",w)
b = AVGy - w * AVGx
print("b的值为：",b)
