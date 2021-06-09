Generate handwritten numbers from 1 to 9
########################################

Introduction
************

生成手写体数字图片的处理顺序:

#. 新建空白图像
#. 生成随机数 1-9
#. 将数字写到空白图像上
#. 旋转和扭曲处理
#. 得到 “手写体数字” 图片

具体实现的函数:

#. 新建 9 个文件夹 ``number_1`` 到 ``number_9``, 分别用于之后存放数字 1-9 图片;

   .. code-block:: bash

      mkdir_for_images()
    

#. 删除子文件夹 ``number_1~9`` 中的所有图片;

   .. code-block:: bash

      clear_images()

#. 生成单张手写体随机数图片;

   .. code-block:: bash

      generate_single()

#. 生成 n 次手写体数字 1-9，并存入指定文件夹 ``number_1~9``;

   .. code-block:: bash

      generate_number_1_to_9(n)


生成的手写体数字图片:

   .. image:: README_number_2.png
      :align: center

For more details, please visit my blog (in chinese): https://www.cnblogs.com/AdaminXie/p/8379749.html;

Thanks for your support.
