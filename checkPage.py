# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec


# 默认chrome驱动放在python目录下
driver = webdriver.Chrome()
driver.get("https://www.mgtv.com")
time.sleep(5)
print(ec.title_contains("芒果"))
