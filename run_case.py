'''
此模块用于运行测试用例

'''
import unittest
from config.config import *
from public.utils.HTMLTestRunner3_New import HTMLTestRunner
from time import strftime

discover = unittest.defaultTestLoader.discover(start_dir=testcase_path,
                                               pattern="test*.py")
# now = strftime("%Y-%m-%d_%H_%M_%S")
f = open("./report/report.html", "wb")
runner = HTMLTestRunner(stream=f,
                        title="cms_ui_auto_report",
                        description="用例执行情况如下",
                        tester="蒋清清")
runner.run(discover)

# import threading
# # from time import sleep,ctime
# from testcase.test001_login import *
# from testcase.test002_usercenter import *
# a=threading.Thread(target=Test_login,args=(1,))
# b=threading.Thread(target=Test_Usercenter,args=(2,))
# a.run()
# b.run()


