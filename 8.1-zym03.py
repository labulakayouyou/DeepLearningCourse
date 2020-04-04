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
x1 = tf.reduce_mean(x)
y1 = tf.reduce_mean(y)
UP = tf.constant(0.)
DOWN = tf.constant(0.)
for i in range(10):
    UP += (x[i] - x1) * (y[i] - y1)
    DOWN += (x[i] - x1) * (x[i] - x1)
w = tf.divide(UP, DOWN)
b = y1 - w * x1
""" 报错https://www.cnblogs.com/123456www/p/12584427.html """
tf.compat.v1.disable_eager_execution()
session = tf.compat.v1.Session()
w_ndarray = w.eval(session=session)
b_ndarray = b.eval(session=session)
print("w={}\nb={}".format(w_ndarray, b_ndarray))
