from src import login
from src.JsonConfigManager import JsonConfigManager
import time
user_id = input("Kakao Story ID를 입력해주세요 : ")
user_pw = input("PW를 입력해주세요 : ")
cookie = login.start(user_id, user_pw)
while True:
    JsonConfigManager().checker()
    time.sleep(5)