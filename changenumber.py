import os

def modify_txt(oldtxt_path):
    for oldtxt in os.listdir(oldtxt_path):
        b = []
        txt_root=os.path.join(oldtxt_path+oldtxt)
        with open(txt_root,'r',encoding='utf-8') as f:
            _txt=f.readlines()# 读取所有行，readlines返回的是列表
            for i in _txt:
                b.append(i.split(' '))  #以空格分开
                for x in b:
                    if x[0]=='32':  #这里换成你想要改的类别
                        x[0]='11'
                #print(b)
            with open(txt_root,'w+',encoding='utf-8') as f: #把列表b里的信息再重新写入
                for c in b:
                    f.writelines(' '.join(c))
if __name__ == "__main__":
    p='D:\pycharmPro\split data\coco3200new\labels/val/'#换成自己的路径，路径中不要出现中文，否则无法识别
    modify_txt(p)

