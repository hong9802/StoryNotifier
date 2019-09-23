from selenium import webdriver
from bs4 import BeautifulSoup
from src import data
import requests
import json

def start(user_id, user_pw):
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://story.kakao.com")
    driver.find_element_by_name("email").send_keys(user_id)
    driver.find_element_by_name("password").send_keys(user_pw)
    driver.find_element_by_xpath("""//*[@id="login-form"]/fieldset/div[8]/button""").click()
    driver.implicitly_wait(3)
    source = driver.page_source
    print(source)
    cookies_list = driver.get_cookies()
    cookies_dict = {}
    driver.close()
    for cookie in cookies_list:
        cookies_dict[cookie['name']] = cookie['value']
    cookie = "_kadu="+cookies_dict['_kadu']+"; TIARA="+cookies_dict['TIARA']+"; _kawlt="+cookies_dict['_kawlt']+"; _kawltea="+cookies_dict['_kawltea'] +"; _karmt="+cookies_dict['_karmt']+"; _karmtea="+cookies_dict['_karmtea']
    data.cookie = cookie
    return cookie