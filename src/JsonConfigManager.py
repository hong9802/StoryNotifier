import os
import json
from src import data
from src import notifier

class JsonConfigManager:
    def __init__(self):
        if(not os.path.isfile(os.getcwd() + "/config.json")):
            print("you need to initallize notify")
            notifier.init_noti(data.cookie)
            self.update()
        else:
            pass #cookie checker with json file load & login passed

    def checker(self):
        parse_data = notifier.init_noti(data.cookie)
        with open("config.json") as json_file:
            config_json = json.load(json_file)
        tmp_json = {
            "created_at" : data.created_at,
            "message" : data.message,
            "content" : data.content,
            "story_id" : data.story_id
        }
        if(config_json != tmp_json):
            notifier.notify(parse_data, config_json)
            self.update()

    def update(self):
        notifier.init_noti(data.cookie)
        tmp_json = {
            "created_at" : data.created_at,
            "message" : data.message,
            "content" : data.content,
            "story_id" : data.story_id
        }
        with open("config.json", 'w', encoding="utf-8") as make_file:
            json.dump(tmp_json, make_file, ensure_ascii=False, indent="\t")