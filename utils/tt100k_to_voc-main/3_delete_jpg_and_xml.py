import os
import glob

# 删除txt中id对应XML和图片
def delete_train_jpg(train_txt):
    root_dir = os.getcwd()
    for line in open(train_txt ,"r"):
        file_id = line.strip()
        # print(file_id)
        file_path = os.path.join(root_dir,"train",file_id+'.jpg')
        # print(file_path)
        os.remove(file_path)


def delete_test_jpg(test_txt):
    root_dir = os.getcwd()
    for line in open(test_txt ,"r"):
        file_id = line.strip()
        # print(file_id)
        file_path = os.path.join(root_dir,"test",file_id+'.jpg')
        # print(file_path)
        os.remove(file_path)

def delete_train_xml(train_txt):
    root_dir = os.getcwd()
    root_path = os.path.join(root_dir,"xmlLabel1")
    for line in open(train_txt,"r"):
        file_id = line.strip()
        # print(file_id)
        file_path = os.path.join(root_path,"train",file_id+'.xml')
        # print(file_path)
        os.remove(file_path)

def delete_test_xml(test_txt):
    root_dir = os.getcwd()
    root_path = os.path.join(root_dir,"xmlLabel1")
    for line in open(test_txt,"r"):
        file_id = line.strip()
        # print(file_id)
        file_path = os.path.join(root_path,"test",file_id+'.xml')
        # print(file_path)
        os.remove(file_path)
if __name__ == '__main__':
    train_txt = "Not_TT45_list_train.txt"
    test_txt = "Not_TT45_list_val.txt"
    delete_train_jpg(train_txt)
    delete_train_xml(train_txt)
    delete_test_jpg(test_txt)
    delete_test_xml(test_txt)