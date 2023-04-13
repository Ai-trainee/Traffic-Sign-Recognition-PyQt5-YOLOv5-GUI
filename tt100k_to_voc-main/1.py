# @Time : 2023-02-18 21:15
# @Author : AItrainee
# @File : 1.py
#计算E:\Desktop\tt100k_to_voc-main\xmlLabel1\train下的xml文件的数量
import os
#获取当前文件夹下的文件名称列表
path = r'E:\Desktop\tt100k_to_voc-main\xmlLabel1\test'
filelist = os.listdir(path)
#统计文件夹下文件个数
total_num = len(filelist)
print(total_num)

