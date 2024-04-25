import os
import shutil

# 所有标签存放路径
path = 'D:\pycharmPro\split data/tiaoxuan\labels'  #文件夹中不能有同名文件
os.chdir(path)
# 文件列表
files = []
################ 用于遍历路径下的文件以及文件夹里的文件#############################
for tuples in os.walk(path):  # 遍历路径下的文件夹及文件 获得多个元组
    path1 = tuples[0] + '\\'
    for content in tuples:    # 遍历元祖
        if type(content) == list:
            for file in content:  # 遍历元组中的列表
                if file.endswith('.txt'):  # 将列表中的txt文件提取出来
                    files.append(path1 + file)  # 将txt文件的路径加到files列表中
###############################################################################

################ 用于遍历路径下的文件，文件夹里的文件不操作#####################
# for file in os.listdir(path):
#     if file.endswith(".txt"):
#         files.append(path + file)
#######################################################################
for file in files:
    with open(file, 'r') as f:
        content = f.readlines()
    for line in content:
        if line[0] == '9':
            shutil.move(file, 'D:\pycharmPro\split data/tiaoxuan/9')  # 类别为5的标签存放路径
            break