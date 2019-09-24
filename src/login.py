from selenium import webdriver
from bs4 import BeautifulSoup
from src import data
import requests
import json
import time

def start(user_id, user_pw):
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
    driver = webdriver.Chrome("./chromedriver", options=options)
    driver.get("https://story.kakao.com")
    driver.find_element_by_name("email").send_keys(user_id)
    driver.find_element_by_name("password").send_keys(user_pw)
    driver.find_element_by_xpath("""//*[@id="login-form"]/fieldset/div[8]/button""").click()
    time.sleep(5)
    source = driver.page_source
    cookies_list = driver.get_cookies()
    cookies_dict = {}
    driver.close()
    for cookie in cookies_list:
        cookies_dict[cookie['name']] = cookie['value']
    cookie = "_kadu="+cookies_dict['_kadu']+"; TIARA="+cookies_dict['TIARA']+"; _kawlt="+cookies_dict['_kawlt']+"; _kawltea="+cookies_dict['_kawltea'] +"; _karmt="+cookies_dict['_karmt']+"; _karmtea="+cookies_dict['_karmtea']
    data.cookie = cookie
    print("login success")
    return cookie