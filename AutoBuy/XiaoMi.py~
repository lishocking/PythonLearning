#coding=utf-8
from selenium import webdriver
import os
import _thread
import time
login_url="https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fitem.mi.com%252Fproduct%252F6334.html%26sign%3DYjY2MTc4Y2FhOWE5M2I0YmI5ZjIyZDI4Yzk0NWU0MTE1NWRkZjRkZA%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180"
req_url = "https://item.mi.com/product/10000085.html"
def openbrowser(login_url,req_url):
    browser = webdriver.Firefox()
    browser.get(login_url)
    username=browser.find_element_by_id("username").send_keys("18500986957")
    passwd=browser.find_element_by_id("pwd").send_keys("fatboy0506")
    login=browser.find_element_by_id("login-button").submit()
    time.sleep(4)
    browser.get(req_url)
    time.sleep(4)
    button1=browser.find_element_by_xpath("//li[@data-name='8GB+256GB 尊享版']")
    button1.click()
    button=browser.find_element_by_xpath("//ul[@id='J_buyBtnBox']/li")
    while(1):
        button.click()
        time.sleep(0.1)
try:
   _thread.start_new_thread( openbrowser, (login_url, req_url, ) )#1
   '''  _thread.start_new_thread( openbrowser, (login_url, req_url, ) )#2
   _thread.start_new_thread( openbrowser, (login_url, req_url, ) )#3
   _thread.start_new_thread( openbrowser, (login_url, req_url, ) )#4
   _thread.start_new_thread( openbrowser, (login_url, req_url, ) )#5'''
   
   
except:
   print ("Error: unable to start thread")

# 打开浏览器

