# 2018-01-9
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie/
# del_pngs.py
# 删除路径下生成的图像文件

import os

path_pic = "F:/code/python/P_generate_handwritten_number/data_pngs/"

#删除路径下的图片
def del_pic():
    for i in range(1, 10):
     #   print(path_png+chr(i))
        namedir = os.listdir(path_pic+str(i))

        for tmppng in namedir:
            if( tmppng in namedir):
              #  print(tmppng)
                os.remove(path_pic+str(i)+"/"+tmppng)

del_pic()
