'''
此模块用于编写登录的测试用例
一个模块一个类，一个类就是一条测试用例

'''
from selenium import webdriver

from public.pages.basepage import BasePage
from selenium import webdriver
from time import sleep

from public.utils.read_ini import Read_Ini
import os
from config.config import *
from data.input_elem import Elem_Input

file = os.path.join(data_path, "data.ini")
r = Read_Ini(file)
url = r.read_ini_data("test_data", "url")
username = r.read_ini_data("test_data", "username")
password = r.read_ini_data("test_data", "passwd")
vertify = r.read_ini_data("test_data", "vertify")


class Test_login(BasePage):
    @classmethod
    def setUpClass(cls) -> None:
        driver = webdriver.Chrome()
        BasePage.set_driver(driver)

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(2)

    def test_login(self):
        browser = BasePage.get_driver()
        browser.get(url)
        BasePage.max()

        elem1 = BasePage.serach_element(Elem_Input.cms_account_input)
        BasePage.sendkeys(elem1, username)
        sleep(1)
        elem2 = BasePage.serach_element(Elem_Input.cms_passwd_input)
        BasePage.sendkeys(elem2, password)
        sleep(1)
        elem3 = BasePage.serach_element(Elem_Input.cms_vertify_input)
        BasePage.sendkeys(elem3, vertify)
        sleep(1)
        elem4 = BasePage.serach_element(Elem_Input.cms_loginbuton_input)
        BasePage.click(elem4)
        try:  # 如果不报错那么就执行它下面的

            elem4 = BasePage.serach_element(Elem_Input.desk_top_input)
            value = BasePage.text(elem4)
            assert value == "系统后台"  # 也可以用self.assertEqual(value,"我的桌面")
        except Exception as e:  # Exception表示报错信息
            print(e)
            BasePage.shoot_png("D/error.png")
        finally:
            pass


if __name__ == '__main__':
    unittest.main()
