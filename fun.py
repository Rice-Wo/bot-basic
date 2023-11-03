import sys
import os
import json
import logging.config


#logging設定
with open('log/log_config.json', "r", encoding='utf-8') as f: # 讀取log設定json檔案
    log = json.load(f)

logging.config.dictConfig(log)
logger = logging.getLogger()

def handle_exception(exc_type, exc_value, exc_traceback): #設定發生問題時的處理方式
    logger.error("程式碼發生錯誤或例外", exc_info=(exc_type, exc_value, exc_traceback))
sys.excepthook = handle_exception

def writeJson(file, item): #JSON寫入
    with open(file + '.json', "w+", encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False, indent=4))
   # logging.debug(f'寫入資料至 {file}.json 資料內容{item}')


def readJson(file): #JSON讀取
    with open(file + '.json', "r", encoding='utf-8') as f:
        data = json.load(f)
    return data
