import sys
import os

import os
import shutil

source_dir = os.path.abspath("../wmydjd")
target_dir = os.path.abspath("../../../../Server/LoadTest/wmydjd")
exclude_dirs = ['__pycache__','.idea','logs']

postfix = ['.py', '.bat', '.sh']  # 指定文件后缀名

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

def is_excluded(file_path):
    for sub_str in exclude_dirs:
        if sub_str in file_path:
            return True
    return False

def copyFile(sourcePath, savePath):
    items = os.listdir(sourcePath)
    for item in items:
        filePath = os.path.join(sourcePath, item)
        if os.path.isfile(filePath):
            if os.path.splitext(filePath)[1] in postfix:  # 后缀名判断
                shutil.copyfile(filePath, os.path.join(savePath, item))  # 复制文件到目标文件夹
                print(' 复制成功 ' + filePath)
            else:
                continue
        elif os.path.isdir(filePath) and not is_excluded(filePath):
            subSavePath = os.path.join(savePath,item)
            print ('拷贝文件夹' + subSavePath)
            copyFile(filePath, subSavePath)  # 如果是文件夹，则再次调用此函数，递归处理
        else:
            print('忽略目标文件或文件夹 ' + filePath)


if __name__ == '__main__':

    copyFile(source_dir, target_dir)


