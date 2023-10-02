import xml.etree.ElementTree as ET

import pickle
import os
from os import listdir, getcwd
from os.path import join
import glob

ls={
    "i2":1,
    "i4":2,
    "i5":3,
    "il100":4,
    "il60":5,
    "il80":6,
    "io":7,
    "ip":8,
    "p10":9,
    "p11":10,
    "p12":11,
    "p19":12,
    "p23":13,
    "p26":14,
    "p27":15,
    "p3":16,
    "p5":17,
    "p6":18,
    "pg":19,
    "ph4":20,
    "ph4.5":21,
    "ph5":22,
    "pl100":23,
    "pl120":24,
    "pl20":25,
    "pl30":26,
    "pl40":27,
    "pl5":28,
    "pl50":29,
    "pl60":30,
    "pl70":31,
    "pl80":32,
    "pm20":33,
    "pm30":34,
    "pm55":35,
    "pn":36,
    "pne":37,
    "po":38,
    "pr40":39,
    "w13":40,
    "w32":41,
    "w55":42,
    "w57":43,
    "w59":44,
    "wo":45
}
#
classes = []# 输入缺陷名称，必须与xml标注名称一致
#classes =ls.keys()
for i in ls.keys():
    classes.append(i)
print(classes)



def convert(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)



# 注意如果是在windows系统下那么路径里的反斜杠\应该多写一个，否则会和python的‘\’产生语义冲突
def convert_annotation(image_name):
    in_file = open(r'E:\Desktop\新建文件夹 (3)\Annotations\%s' % (image_name))  # 读取xml文件路径

    out_file = open(r'E:\Desktop\新建文件夹 (3)\%s.txt' % (image_name), 'w')  # 需要保存的txt格式文件路径
    f = in_file
    xml_text = f.read()
    root = ET.fromstring(xml_text)
    f.close()

    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            print(cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()

if __name__ == '__main__':

    filenames = os.listdir( r"E:\Desktop\新建文件夹 (3)\Annotations")  # xml文件路径，这样输出的txt文件和xml一一对应

    for label_path in filenames:
        print(label_path)
        convert_annotation(label_path)

