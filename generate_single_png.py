# 2018-01-9
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie/
# generate_single_png.py
# 生成手写体数字/字母/汉字


import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

random.seed(3)

# 生成单张扭曲的数字图像
def generate_single():

    # 先绘制一个50*50的空图像
    img_50_blank = Image.new('RGB', (50, 50), (255, 255, 255))

    # 创建画笔
    draw = ImageDraw.Draw(img_50_blank)

    # 设置字体，这里选取字体大小25
    font = ImageFont.truetype('simsun.ttc', 20)

    # xy是左上角开始的位置坐标
    # text是你想要显示的内容，数字/字母/汉字
    char ="呵"
    draw.text(xy=(12, 11), font=font, text=char, fill=(0, 0, 0))

    # 随机旋转-10-10角度
    random_angle = random.randint(-10, 10)
    img_50_rotated = img_50_blank.rotate(random_angle)

    # 图形扭曲参数
    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500]

    # 创建扭曲
    img_50_transformed = img_50_rotated.transform((50, 50), Image.PERSPECTIVE, params)

    # 生成新的30*30空白图像
    img_30 = img_50_transformed.crop([10, 10, 40, 40])

    return img_30, char

path_pic = "F:/code/python/P_generate_handwritten_number/"


# 调用生成图像文件函数
img, generated_char = generate_single()
imgray = img.convert('1')

print(path_pic + "test.png")
# 将图像保存在指定文件夹中
imgray.save(path_pic + "test.png")
