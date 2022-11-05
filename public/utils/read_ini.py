'''
封装一个专门读取INI文件的工具
读取INI文件中内容需要下载configparser的包，这个包里存储了用来读取ini文件的类和方法
下载方式：到dos窗口，输入：pip install configparser
'''
from configparser import ConfigParser
from config.config import *
import os


# c=ConfigParser()
# c.read(file,encoding="utf-8")
# print(c.get("test_data","url"))
# 上述方法不方便

class Read_Ini(ConfigParser):
    def __init__(self, file):
        super(Read_Ini, self).__init__()  # 继承父类构造函数
        self.read(file, encoding="utf-8")  # 读取文件中的内容

    def read_ini_data(self, section, option):
        value = self.get(section, option)
        return value


if __name__ == '__main__':
    file1 = os.path.join(data_path, "data.ini")
    r = Read_Ini(file1)
    print(r.read_ini_data("test_data", "url"))

# class Read(ConfigParser):
#     def __init__(self,file):
#         super(Read, self).__init__()
#         self.read(file,encoding="utf-8")
#     def read_data(self,section,option):
#          value=self.get(section,option)
#          return value
# file1=os.path.join(data_path, "data.ini")
# r=Read(file1)
# print(r.read_data("test_data","username"))
# print(r.read_data("test_data","passwd"))
