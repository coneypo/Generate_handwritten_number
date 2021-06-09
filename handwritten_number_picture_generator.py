# Author:       coneypo
# Blog:         http://www.cnblogs.com/AdaminXie/
# Github:       https://github.com/coneypo/Generate_handwritten_number
# 生成手写体数字 / Generate handwritten numbers from 1~9


import random
import os
from PIL import Image, ImageDraw, ImageFont

random.seed(3)
path_img = "data_pngs/"


# 在目录下生成用来存放数字 1-9 的 9 个文件夹，分别用 number_1-9 命名 / mkdir folders with name 'number_1' to 'number_9'
def mkdir_for_images():
    if not os.path.isdir(path_img):
        os.mkdir(path_img)
    for i in range(1, 10):
        if os.path.isdir(path_img + "number_" + str(i)):
            pass
        else:
            print(path_img + "number_" + str(i))
            os.mkdir(path_img + "number_" + str(i))


mkdir_for_images()


# 删除路径下的图片 / Clear images in 'data/pngs/number_x/'
def clear_images():
    for i in range(1, 10):
        dir_nums = os.listdir(path_img+ "number_"  + str(i))
        for tmp_img in dir_nums:
            if tmp_img in dir_nums:
                # print("delete: ", tmp_img)
                os.remove(path_img + "number_" + str(i) + "/" + tmp_img)
    print("Delete finish", "\n")


clear_images()


# 生成单张扭曲的数字图像 / Generate a single distorted digital image
def generate_single():
    # 先绘制一个 50*50 的空图像 / Draw a blank image with size 50*50
    im_50_blank = Image.new('RGB', (50, 50), (255, 255, 255))

    # 创建画笔 / Create drawer
    draw = ImageDraw.Draw(im_50_blank)

    # 生成随机数 1-9 / Generate random number from 1-9
    num = str(random.randint(1, 9))

    # 设置字体，这里选取字体大小 25 / Set font
    font = ImageFont.truetype('simsun.ttc', 20)

    # xy 是左上角开始的位置坐标 / xy is the position starts
    draw.text(xy=(18, 11), font=font, text=num, fill=(0, 0, 0))

    # 随机旋转-10-10角度 / Rotate with an angle of -10 to 10 randomly
    random_angle = random.randint(-10, 10)
    im_50_rotated = im_50_blank.rotate(random_angle)

    # 图形扭曲参数 / Distortion parameters
    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500]

    # 创建扭曲 / Do distortion 
    im_50_transformed = im_50_rotated.transform((50, 50), Image.PERSPECTIVE, params)

    # 生成新的 30*30 空白图像 / Generate blank image with size 30*30
    im_30 = im_50_transformed.crop([10, 10, 40, 40])

    return im_30, num


# 生成手写体数字 1-9 存入指定文件夹 1-9 / Generate 1-9
def generate_number_1_to_9(n):
    cnt_num = []

    for i in range(10):
        cnt_num.append(0)

    for m in range(1, n + 1):
        img, generate_num = generate_single()
        img_gray = img.convert('1')

        for j in range(1, 10):
            if generate_num == str(j):
                cnt_num[j] = cnt_num[j] + 1
                print("Generate:", path_img + "number_" + str(j) + "/" + str(j) + "_" + str(cnt_num[j]) + ".png")
                img_gray.save(path_img + "number_" + str(j) + "/" + str(j) + "_" + str(cnt_num[j]) + ".png")

    print("\n")
    print("生成的数字 1-9 的分布 / Distribution of generated numbers 1-9：")
    for k in range(9):
        print("number", k + 1, ":", cnt_num[k + 1], "in all")


def main():
    # 运行 1000 次 / Run 100 times
    generate_number_1_to_9(100)


if __name__ == '__main__':
    main()