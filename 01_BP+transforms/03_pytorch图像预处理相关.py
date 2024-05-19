# @Date ：2024/05/19 12:37
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from torchvision import transforms
from PIL import Image

def t1():
    img = Image.open("小狗.png")
    ts = transforms.Compose(
        transforms = [
            transforms.ToTensor(),  # PIL转化为tensor对象
            transforms.RandomOrder(
                transforms=[
                    transforms.RandomPerspective(),
                    transforms.RandomRotation(degrees=30),
                    transforms.RandomAffine(degrees=30),
                    transforms.RandomErasing(),
                    # transforms.RandomPosterize(bits=5),
                    transforms.Resize(size=(224, 224)),  # 将图像resize到自己想要的大小
                ]
            ),
            # transforms.RandomPerspective(),
            # transforms.Resize(size=(224, 224)), # 将图像resize到自己想要的大小
            # transforms.CenterCrop(size=(200, 100)),  # 中心裁剪
            transforms.RandomCrop(size=(150, 200)),

            # transforms.Normalize(mean=[0.2, 0.7, 0.5], std=[0.5, 0.7, 0.6]) # 均值化


        ]
    )
    ts2 = transforms.Compose(
        transforms = [
            transforms.ToPILImage() # tensor转化为PIL对象
        ]
    )
    tensor = ts(img)
    print("tensor", tensor)
    img2 = ts2(tensor)
    img2.show()

    img3 = ts2(ts(img))
    img3.show()

    print(tensor.size())


if __name__ == '__main__':
    t1()