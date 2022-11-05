from public.pages.basepage import BasePage
from selenium import webdriver
from time import sleep
from public.utils.read_ini import Read_Ini
import os
from config.config import *
from data.input_elem import Elem_Input

class Test_Usercenter(BasePage):

    def test_location(self):

        elem1=BasePage.serach_element(Elem_Input.yhq_sc_input)
        BasePage.click(elem1)
        sleep(1)
        elem2=BasePage.serach_element(Elem_Input.yhq_cx_input)
        BasePage.click(elem2)
        sleep(1)
        elem3=BasePage.serach_element(Elem_Input.yhq_yhq_input)
        BasePage.click(elem3)
        sleep(1)
        elem4=BasePage.serach_element(Elem_Input.yhq_iframe_input)
        BasePage.switch_iframe(elem4)
        sleep(1)
        elem5=BasePage.serach_element(Elem_Input.yhq_list_input)
        vlaue=BasePage.text(elem5)

        assert vlaue == "优惠券列表"

        sleep(3)

