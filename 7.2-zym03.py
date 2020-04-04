# -*- coding: utf-8 -*-
"""
要求：

(1)下载手写数字数据集，读取训练集和测试集数据，放在NumPy数组train_x、train_y、test_x、test_y中；
（train_x：训练集图像，train_y：训练集标签，test_x：测试集图像，test_y：测试集标签）
(2)随机从所有测试集数据中显示16幅数字图像；
(3)16幅图像按照4×4方式排列在一张画布中，每幅图像的子标题为该图像的标签值，字体大小为14，全局标题
为“MNIST测试集样本”，字体大小为20，颜色为红色。
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
mnist=tf.keras.datasets.mnist
(train_x,train_y),(test_x,test_y)=mnist.load_data()

for i in range(16):
    num=np.random.randint(1,60000)
    plt.subplot(4,4,i+1)
    plt.imshow(train_x[num],cmap='gray')
    plt.title(train_y[num],fontsize=14)
    
plt.subtitle("MNIST测试集样本",fontsize=20,color="red")
