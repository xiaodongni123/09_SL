# @Date ：2024/05/18 21:35

from PIL import Image, ImageFilter,ImageEnhance
import numpy as np
import copy, collections


def t1():
    img = Image.open(fp="小狗.png")
    print(type(img))
    # img.save("d.bmp")
    w, h = img.size
    print(img.format, img.size, img.mode)
    # img.show("aa")

    img_arr = np.array(img)
    # 这两行代码用于处理二维图像数组，将其转换为三维数组
    if len(img_arr.shape) == 2:
        img_arr = img_arr[:, :, None]
    print(img_arr.shape)
    print(img_arr[:2, :2, :])

    # 既然这是一个numpy数组，那么可以对里面的数字做任何处理
    img_arr1 = copy.deepcopy(img_arr)
    img_arr1[:100, :100, :3] = 0
    img1 = Image.fromarray(img_arr1, img.mode)   #Image.fromarray函数将修改后的数组img_arr1转换回一个图像对象
    print("img1", img1)
    img1.save("img1.png")

    # 随机mask掩盖一部分图像区域
    img_arr2 = copy.deepcopy(img_arr)
    h1 = np.random.randint(low=0, high=h-100)
    w1 = np.random.randint(low=0, high=w-100)
    img_arr2[h1:h1+100, w1:w1+100, :3] = 0
    img2 = Image.fromarray(img_arr2, img.mode)
    img2.save("img2.png")

    # 随机mask掉5个图片
    for i in range(5):
        img_arr2 = copy.deepcopy(img_arr)
        s = np.random.randint(50, 200)
        h1 = np.random.randint(low=0, high=h - s)
        w1 = np.random.randint(low=0, high=w - s)
        img_arr2[h1:h1 + s, w1:w1 + s, :3] = 0
        img2 = Image.fromarray(img_arr2, img.mode)
        img2.save(f"img_{i}.png")

def t2():
    img:Image.Image = Image.open("小狗.png")
    # 1.img是RGB图片, 转换成灰度图像
    img1 = img.convert("L")
    # img1.show()
    img1.save("e.png")

    # 2.灰度图像转换成黑白图像（二值化图像的操作）
    img1_arr = np.array(img1).reshape(-1) # 将图像 img1 转换为一个 NumPy 数组，并将其展平成一维数组。
    counter = collections.Counter(img1_arr)
    img2 = img1.point(lambda i:255 if i>250 else 0)
    # img2.show()

    # 3. 大小缩放 (按双线性插值等方式)
    img3 = img.resize((300, 250), resample=Image.NEAREST)
    # img3.show()

    # 4. 图像的旋转
    img4 = img.rotate(angle=20, expand=True)
    # img4.show()

    # 5. 图像的翻转(水平翻转，左右翻转)
    # img5 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img5 = img.transpose(Image.FLIP_TOP_BOTTOM)
    # img5.show()

    # 6.剪切
    box = (300, 0, 900, 300)
    img6 = img.crop(box)
    # img6.show()

    # 7. 图像分裂，合并
    r, g, b = img6.split()
    r = r.point(lambda i: i+100)
    # img7 = Image.merge("RGB", (g, b, r)) # 把g当做r, 把b当成g， 把r当成b
    img7 = Image.merge("RGB", (r, g, b))
    # img7.show()

    # 8. 图像粘贴
    img.paste(img7, box)
    img.show()

def t3(i=None):
    img = Image.open("小狗.png")

    # 1. 使用高斯滤波器
    img1 = img.copy()
    for i in range(10):
        img1 = img1.filter(ImageFilter.GaussianBlur)
    # img.show()

    # 2.锐度增强
    enhancer = ImageEnhance.Sharpness(img)
    for i in range(1, 8):
        factor = i / 2.0
        enhancer.enhance(factor).show("sharpness % f" % factor)

if __name__ == '__main__':
    # t1()
    # t2()
    t3()