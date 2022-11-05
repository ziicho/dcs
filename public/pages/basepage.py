'''
此模块用于封装页面的操作和基类
包含创建浏览器对象，元素定位，元素操作（点击，输入，悬停。。。）
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#driver=webdriver.Chrome()

class BasePage(unittest.TestCase):
    @classmethod
    def set_driver(cls,browser_driver):
        cls.driver=browser_driver
    @classmethod
    def get_driver(cls):
        return cls.driver
    @classmethod
    def serach_element(cls,element):
        type=element[0]
        value=element[1]
        if type=="id" or type=="ID":
            return cls.driver.find_element(By.ID,value)
        elif type=="name" or type=="NAME":
            return cls.driver.find_element(By.NAME,value)
        elif type=="class" or type=="CLASS":
            return  cls.driver.find_element(By.CLASS_NAME,value)
        elif type=="link_text" or type=="LINK_TEXT":
            return  cls.driver.find_element(By.LINK_TEXT,value)
        elif type=="xpath" or type=="XPATH":
            return cls.driver.find_element(By.XPATH,value)
        elif type=="css" or  type=="CSS":
            return cls.driver.find_element(By.CSS_SELECTOR,value)
        elif type=="tar_name" or type=="TAR_NAME":
            return cls.driver.find_element(By.TAG_NAME,value)
        elif type=="PARTIAL_LINK_TEXT" or type=="partial_link_next":
            return cls.driver.find_element(By.PARTIAL_LINK_TEXT,value)
        else:
            raise ValueError("please input correct parmaeters")

    @classmethod
    def click(cls,elem):
        return elem.click()
    @classmethod
    def sendkeys(cls,elem,value):
        return elem.send_keys(value)
    @classmethod
    def max(cls):
        return cls.driver.maximize_window()
    @classmethod
    def scroll(cls,n):
        for i in range(n):
            return cls.driver.execute_script("window.scrollTo(0,%d)"%i)
    @classmethod
    def switch_iframe(cls,elem):
        return cls.driver.switch_to.frame(elem)
    @classmethod
    def quit_iframe(cls):
        return cls.driver.switch_to_default_content()
    @classmethod
    def move_to_element(cls,elem):
        return ActionChains(cls.driver).move_to_element(elem).perform()
    @classmethod
    def wait(cls):
        return  cls.driver.implicitly_wait()
    @classmethod
    def switch_window(cls,n):
        return cls.driver.switch_to.window(cls.driver.window_handles[n])
    @classmethod
    def quit(cls):
        return cls.driver.quit()
    @classmethod
    def close(cls):
        return cls.driver.close()
    @classmethod
    def back(cls):
        return cls.driver.back()
    @classmethod
    def refresh(cls):
        return cls.driver.refresh()
    @classmethod
    def open_new_window(cls,url):
        js="window.open('%s')"%url
        return driver.execute_script(js)
    @classmethod
    def text(cls,elem):
        return  elem.text
    @classmethod
    def shoot_png(cls,file):
        return cls.driver.get_screenshot_as_file(file)

if __name__ == '__main__':
    driver=webdriver.Chrome()
    BasePage.set_driver(driver)
    a=BasePage.get_driver()
    a.get("http://baidu.com")
    BasePage.max()
    baidu_input=("id","kw")
    elem1=BasePage.serach_element(baidu_input)
    BasePage.sendkeys(elem1,"chengdu20")
    BasePage.open_new_window('http://www.jd.com')
