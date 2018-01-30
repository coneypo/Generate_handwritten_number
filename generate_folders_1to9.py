# 2018-01-9
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie/
# generate_folders_1to9.py
# 在目录下生成用来存放数字1-9的9个文件夹，分别用1-9命名


import os

path_folders = "F:/code/python/P_generate_handwritten_number/data_pngs/"

# 1-9
for i in range(49,58):
    if (os.path.isdir(path_folders + chr(i))):
        pass
    else:
        # print(i,": ",path_1+chr(i))
        # 生成目录
        os.mkdir(path_folders+chr(i))
