# -*- coding:utf-8 -*-

from selenium import webdriver
import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# 默认 chrome 驱动放在 python 目录下
driver = webdriver.Chrome()
driver.get("https://www.mgtv.com")
time.sleep(5)

# clickElement.py 中通过元素来判断是否有弹出的隐私政策block
# 现在使用 selenium 的 WebDriverWait 来判断规定时间内某个元素是否可见
locator = (By.CLASS_NAME, "m-agreement-mask")
# return element or False
visible = WebDriverWait(driver, 3).until(ec.visibility_of_element_located(locator))
print(visible)
if visible is not False:
    print("Can be seen")


driver.close()
