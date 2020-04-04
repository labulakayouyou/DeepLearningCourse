# -*- coding: utf-8 -*-
"""
使用TensorFlow张量运算计算w和b，并输出结果。
已知： 
x=[ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
y=[ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]
"""

import tensorflow as tf
import numpy as np
x = tf.constant([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
sum_xy = tf.constant(0.)
sum_x = tf.constant(0.)
sum_y = tf.constant(0.)
sum_x2 = tf.constant(0.)
for i in range(10):
    sum_xy += x[i]*y[i]
    sum_x += x[i]
    sum_y += y[i]
    sum_x2 += x[i]*x[i]
w = tf.divide(sum_xy-sum_x*sum_y, sum_x2-sum_x*sum_x)
b = tf.divide(sum_y-w*sum_x, 10)

""" 报错https://www.cnblogs.com/123456www/p/12584427.html """
tf.compat.v1.disable_eager_execution()
session = tf.compat.v1.Session()
w_array = session.run(w)
b_array = session.run(b)
print("w={}\nb={}".format(w_array, b_array))
