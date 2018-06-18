# del_content 要删除的关键字（例如广告词）
import os

def rename(path, del_content):
    files = os.listdir(path)
    for f in files:
        orgin_name = os.path.join(path, f)
        new_name = os.path.join(path, f.replace(del_content, ""))
        os.rename(orgin_name, new_name)
        if os.path.isdir(new_name):
            rename(new_name, del_content)

rename("c:/def", "[广告]")

# path 加密的文件路径
# path2 加密之后生成的文件路径 ，用异或操作可以实现回来

def encrypt(path, path2):
    with open(path, "rb") as f, open(path2, "wb") as f2:
        for line in f:
            for v in line:
                f2.write(bytes([v ^ 10]))

# encrypt("c:/def/2.txt", "c:/def/en.txt")
encrypt("c:/def/en.txt", "c:/def/restore.txt")