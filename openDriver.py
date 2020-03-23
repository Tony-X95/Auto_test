# -*- coding:utf-8 -*-

from selenium import webdriver


# 直接引用chromedriver.exe
# chrome_driver = r"D:\ChromeDownload\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver)

# chromedriver.exe放在python目录下或以配置环境变量时
driver = webdriver.Chrome()
driver.get("https://www.mgtv.com")
