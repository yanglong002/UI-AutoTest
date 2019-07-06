from selenium import webdriver
import time


dr = webdriver.Chrome()
time.sleep(5)
dr.get("https://www.baidu.com")
time.sleep(5)
print(dr.name)
dr.quit()