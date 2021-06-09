Generate handwritten numbers from 1 to 9
########################################

Introduction
************

新建空白图像 >>> 生成随机数 1-9 >>> 将数字写到空白图像上 >>> 旋转&扭曲 处理 >>> 得到 “手写体数字”

For more details, please visit my blog (in chinese): https://www.cnblogs.com/AdaminXie/p/8379749.html

#.新建9个文件夹 Num_1-Num_9，分别用于之后存放数字1-9图片;

   .. code-block:: bash

      mkdir_for_imgs()
    

#. 删除子文件夹 Num_1-9 中的所有图片;

   .. code-block:: bash

      del_imgs()

#. 生成单张手写体随机数图片;

   .. code-block:: bash

      generate_single()

#. 生成 n 次手写体数字 1-9，并存入指定文件夹 Num_1-Num_9;

   .. code-block:: bash

      generate_1to9(n):



生成的手写体数字

   .. image:: README_Num_2.png
      :align: center



Thanks for your support.
