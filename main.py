import tkinter as tk
import os
import logging
from fun import readJson, writeJson
import discord
from windows import error_window
from pathlib import Path
from discord.ext import commands
from datetime import datetime
import time


#設定日誌
logs_folder = "logs"
os.makedirs(logs_folder, exist_ok=True)

current_time = datetime.now()
log_filename = f"log_{current_time.strftime('%Y-%m-%d_%H.%M.%S')}.log"
log_path = os.path.join(logs_folder, log_filename)

logging.basicConfig(
	level=logging.INFO,
	format='%(asctime)s [%(levelname)s] : %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
)

file_handler = logging.FileHandler(log_path) #log檔紀錄
file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
logging.getLogger().addHandler(file_handler)


def error_hand(reason): #錯誤處理
	logging.critical(reason)
	root = tk.Tk()
	app = error_window(root, reason)
	root.mainloop()





#discord 機器人
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(status=discord.Status.do_not_disturb, intents = intents)




@bot.event
async def on_ready():
	logging.info(f"機器人 {bot.user} 已經上線了")
	logging.info('請勿關閉本視窗以維持機器人上線狀態，可以最小化')
	logging.info('如要關閉機器人請使用/close指令 或者在本視窗按下ctrl+C')
	loaded_cogs = list(bot.cogs.keys())
	if loaded_cogs:
		for cog_name in loaded_cogs:
			logging.info(f'已載入 {cog_name} 模塊')
	else:
		logging.warning('沒有任何模組被載入，請確認cogs資料夾')







# 如果沒設定檔就創建一個新的設定檔
if not os.path.exists("config.json"):    
	config = {
		'token': "",
		'setting2': 'value2',
		'setting3': 'value3'
	}
	writeJson('config', config)
	config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
	logging.debug(f'已創建config.json，檔案位置 {config_file}')



def tokenInput(): #給使用者輸入token
	T = input('請輸入token')
	config = readJson('config')
	config['token'] = T
	writeJson('config', config)

def run_bot(): #執行機器人
	config = readJson('config')
	try:
		token = config['token']
		bot.run(token)
	except discord.errors.LoginFailure:
		config['token'] = ""
		writeJson('config', config)
		error_hand('token錯誤或過期，請重新輸入')
	except Exception as e:
		error_hand(e)

#載入cog
for filepath in Path("./cogs").glob("**/*.py"):
	cog_name = Path(filepath).stem
	bot.load_extension(f"cogs.{cog_name}")
	logging.debug(f'已載入 {cog_name} 模塊')

if __name__ == "__main__":
	config = readJson('config')
	if config['token']:
		run_bot()
	else:
		tokenInput()
		run_bot()
