from log.logging import handle_exception
import sys

sys.excepthook = handle_exception

import os
import logging
from fun import readJson, writeJson
import discord
from pathlib import Path
from discord.ext import commands
from datetime import datetime
import time





#discord 機器人
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(status=discord.Status.do_not_disturb, intents = intents)




@bot.event
async def on_ready():
	logging.info(f"已使用 {bot.user} 上線了")
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
		logging.critical('token錯誤或過期，請重新輸入')

for filepath in Path("./cogs").glob("**/*cog.py"): #載入cog
	parts = list(filepath.parts)
	parts[-1] = filepath.stem
	bot.load_extension(".".join(parts))
	logging.debug(f'已載入 {parts} 模塊')

if __name__ == "__main__":
	config = readJson('config')
	if config['token']:
		run_bot()
	else:
		tokenInput()
		run_bot()
