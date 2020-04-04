# -*- coding: utf-8 -*-
"""
(1)将R通道的图像缩小为50×50，显示在子图1中，子标题为:“R-缩放”，字体大小为14；
(2)将G通道的图像先水平镜像，再顺时针旋转90度，显示在子图2中，子标题为:“G-镜像+旋转”，字体大小为14，并显示坐标轴；
(3)对B通道的图像进行裁剪，裁剪位置：左上角(0, 0) 右下角(150, 150)，显示在子图3中，子标题为:“B-裁剪”，字体大小为14；
(4)将原始的R、G、B通道的图像合并，显示在子图4中，子标题显示图像的色彩模式，字体大小为14；
(5)将要求(4)的处理结果保存为PNG格式的图片，路径为当前工作目录，文件名为“test.png”，如图2所示；
(6)将以上生成的4幅图像显示在2×2的画布中，全局标题为“图像基本操作”，标题字体大小为20，颜色为蓝色。
"""
""" 
r g b三个颜色通道
cmap="gray"表示各个通道的图像都是以灰度图像的形式显示的
 """
from PIL import Image
import matplotlib.pyplot as plt
img=Image.open("Lena.tiff")
img_r,img_g,img_b = img.split()  
plt.figure(figsize=(10,10))

plt.subplot(221)
plt.axis("off")
img_small=img_r.resize((50,50))
plt.imshow(img_small, cmap="gray")
plt.title("R-缩放",fontsize=14)

plt.subplot(222)
img_flr=img_g.transpose(Image.FLIP_LEFT_RIGHT)
img_r90=img_flr.transpose(Image.ROTATE_270)
plt.imshow(img_r90, cmap="gray")
plt.title("G-镜像+旋转",fontsize=14)

plt.subplot(223)
plt.axis("off")
img_region=img_b.crop((0,0,150,150))
plt.imshow(img_region, cmap="gray")
plt.title("B-裁剪",fontsize=14)

img_rgb = Image.merge("RGB", [img_r,img_g,img_b])
plt.subplot(224)
plt.axis("off")
plt.imshow(img_rgb)
plt.title("img_rgb.format",fontsize=14)
img.save("test.png")

plt.subtitle("图像基本操作",fontsize=20,color="blue")

plt.show()

