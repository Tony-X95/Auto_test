# -*- coding:utf-8 -*-

from selenium import webdriver
import time

# 默认chrome驱动放在python目录下
driver = webdriver.Chrome()
driver.get("https://www.mgtv.com")
time.sleep(5)

# 判断是否有隐私政策block，如果有click同意
pPrivateFlag = driver.find_elements_by_class_name("m-agreement-mask")
print(len(pPrivateFlag))
if len(pPrivateFlag) > 0:
    driver.find_elements_by_class_name("allow").click()

# click，点开注册/登录block
driver.find_element_by_id("honey-header-user").find_element_by_class_name("c-header-login").click()

# 自动填写登录信息
driver.find_element_by_id("honey-mini-login-auto").send_keys("18300000000")
driver.find_element_by_class_name("login-dialog-password").send_keys("1234qwer")
driver.find_element_by_class_name("mini-login-yzm").send_keys("123456")

driver.close()
