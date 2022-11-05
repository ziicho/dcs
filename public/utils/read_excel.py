'''
此模块用于读取excel文件,这个包里存储了用来读取excel文件的类和方法
在dos窗口下载，输入pip istall xlrd
'''

import xlrd
from config.config import *
# workbook=xlrd.open_workbook()这个就可以打开以xlsx结尾的文件
# workbook=xlrd.open_workbook_xls()打开以xls结尾的文件

# sheet1=workbook.sheet_by_name("Sheet1")
# username=sheet1.cell_value(1,0)

class Read_Excel():
    def __init__(self,file,sheet):
        self.workbook=xlrd.open_workbook_xls(file)
        self.sheet1=self.workbook.sheet_by_name(sheet)

    def raed_data(self,rowx,colx):
        return self.sheet1.cell_value(rowx,colx)

if __name__ == '__main__':
    file=os.path.join(data_path,"data.xls")
    r=Read_Excel(file,"Sheet1")
    print(r.raed_data(1,0))
