# 2018-01-9
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie/
# generate_pngs.py
# 生成手写体数字


import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

random.seed(3)

# 生成单张扭曲的数字图像
def generate_single():

    # 先绘制一个50*50的空图像
    img_50_blank = Image.new('RGB', (50, 50), (255, 255, 255))

    # 创建画笔
    draw = ImageDraw.Draw(img_50_blank)

    # 生成随机数1-9
    num = str(random.randint(1, 9))

    # 设置字体，这里选取字体大小25
    font = ImageFont.truetype('simsun.ttc', 20)

    # xy是左上角开始的位置坐标
    draw.text(xy=(18, 11), font=font, text=num, fill=(0, 0, 0))

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

    return img_30, num

path_pic = "F:/code/python/P_generate_handwritten_number/data_pngs/"


# 生成手写体数字1-9存入指定文件夹1-9

# 用cnt_num[1]-cnt_num[9]来计数数字1-9生成的个数，方便之后进行命名
cnt_num = []
for i in range(10):
    cnt_num.append(0)

# 生成次数
samples = 200

for m in range(1, samples+1):

    # 调用生成图像文件函数
    img, generate_num = generate_single()

    # 取灰度
    imgray = img.convert('1')

    # 计数生成的数字1-9的个数,用来命名图像文件
    for j in range(1, 10):
        if(generate_num == str(j)):
            cnt_num[j] = cnt_num[j]+1

            # 路径如 "F:/code/***/P_generate_handwritten_number/data_pngs/1/1_231.png"
            # 输出显示路径
            print(path_pic + str(j) + "/" + str(j) + "_" + str(cnt_num[j]) + ".png")
            # 将图像保存在指定文件夹中
            imgray.save(path_pic + str(j) + "/" + str(j) + "_" + str(cnt_num[j]) + ".png")

# 输出显示1-9的分布
print("\n", "生成的1-9的分布：")
for k in range(9):
    print(k+1, ":", cnt_num[k+1], "张")