from src import data
import requests
import json
import subprocess

def init_noti(cookie):
    headers = {
        "Host" : "story.kakao.com",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Accept" : "application/json",
        "Accept-Language" : "ko",
        "Connection" : "keep-alive",
        "X-Kakao-ApiLevel" : "49",
        "X-Kakao-DeviceInfo" : "web:d;-;-",
        "X-Requested-With" : "XMLHttpRequest",
        "Referer" : "https://story.kakao.com/",
        "Cookie" : cookie
    }
    r = requests.get("https://story.kakao.com/a/notifications", headers=headers)
    notifi_list = r.text
    tmp_noti = json.loads(notifi_list)
    tmp = tmp_noti[0]
    try:
        data.content = tmp['content']
        data.message = tmp['message']
        data.created_at = tmp['created_at']
        data.story_id = tmp['id']
    except KeyError as e:
        data.message = tmp['message']
        data.created_at = tmp['created_at']
        data.story_id = tmp['id']
    return tmp_noti

def notify(parse_data, config_json):
    try:
        tmp_json = {
            "created_at" : parse_data[0]['created_at'],
            "content" : parse_data[0]['content'],
            "message" : parse_data[0]['message'],
            "story_id" : parse_data[0]['id']
        }
    except KeyError as e:
        tmp_json = {
            "created_at" : parse_data[0]['created_at'],
            "content" : "",
            "message" : parse_data[0]['message'],
            "story_id" : parse_data[0]['id']
        }
    if(tmp_json == config_json):
        return
    try:
        subprocess.Popen(['notify-send', parse_data[0]['message'], parse_data[0]['content']])
    except KeyError as e:
        subprocess.Popen(['notify-send', parse_data[0]['message']])