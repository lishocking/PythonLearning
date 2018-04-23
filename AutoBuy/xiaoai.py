#coding=utf-8
from selenium import webdriver
import os
import time
# set little time stop and big time stop for viewing changes
little_time_stop = 1
big_time_stop = 2
# 默认广告条数
ads_num_require = 8
# 请求连接
login_url="https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fitem.mi.com%252Fproduct%252F6334.html%26sign%3DYjY2MTc4Y2FhOWE5M2I0YmI5ZjIyZDI4Yzk0NWU0MTE1NWRkZjRkZA%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180"
req_url = "https://item.mi.com/product/6334.html"
# 打开浏览器

browser = webdriver.Firefox()
# 开始请求
browser.get(login_url)
username=browser.find_element_by_id("username").send_keys("18500986957")
passwd=browser.find_element_by_id("pwd").send_keys("fatboy0506")
login=browser.find_element_by_id("login-button").submit()
time.sleep(10)
browser.get(req_url)
button=browser.find_element_by_id("J_buyBtnBox")
# 下面代码选择取消注释
# 延时
# time.sleep(5)
# 关闭当前窗口
# browser.close()
# 关闭所有已经打开的窗口
# browser.quit()
