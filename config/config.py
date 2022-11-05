'''
存放项目的路径，和每个包的路径

'''
import  os
#__file__表示当前文件
base_path=os.path.dirname(os.path.dirname(__file__))
#print(base_path)
#base_path表示cms_api_auto2这个项目的路径

config_path=os.path.join(base_path,"config")
#print(config_path)
#config包的路径

public_path=os.path.join(base_path,"public")
#print(public_path)
#public包的路径

pages_path=os.path.join(public_path,"pages")
#print(pages_path)

utils_path=os.path.join(public_path,"utils")
#print(utils_path)

report_path=os.path.join(base_path,"report")
#print(report_path)

runcase_path=os.path.join(base_path,"runcase")
#print(runcase_path)

testcase_path=os.path.join(base_path,"testcase")
#print(test_case_path)

data_path=os.path.join(base_path,"data")