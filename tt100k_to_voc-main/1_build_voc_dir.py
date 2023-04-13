import os

# 建立相关文件夹
# build voc2007 folder structure
def make_voc_dir():
    root_dir = os.getcwd()
    os.makedirs(root_dir+'/VOC2007')
    os.makedirs("VOC2007"+'/Annotations')
    os.makedirs("VOC2007" + '/JPEGImages/ ')
    os.makedirs("VOC2007"+'/ImageSets')
    os.makedirs("VOC2007"+'/ImageSets/Main')

if __name__ == '__main__':
    make_voc_dir()