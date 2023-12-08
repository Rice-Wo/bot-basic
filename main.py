from log.logging import handle_exception
import sys

sys.excepthook = handle_exception

import os
import logging
from utility import write_Json, get_Json
import discord
from pathlib import Path





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
			logging.info(f'已載入 {cog_name} 模組')
	else:
		logging.warning('未載入任何模組，請重開機器人')







# 如果沒設定檔就創建一個新的設定檔
if not os.path.exists("config.json"):    
	config = {
		'token': "",
		'setting2': 'value2',
		'setting3': 'value3'
	}
	write_Json('config', config)
	config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
	logging.debug(f'已創建config.json，檔案位置 {config_file}')



def tokenInput(): #給使用者輸入token
	T = input('請輸入token')
	config = get_Json('config')
	config['token'] = T
	write_Json('config', config)

def run_bot(): #執行機器人
	config = get_Json('config')
	try:
		token = config['token']
		bot.run(token)
	except discord.errors.LoginFailure:
		config['token'] = ""
		write_Json('config', config)
		logging.critical('token錯誤或過期，請重新輸入')

for filepath in Path("./cogs").glob("**/*cog.py"): #載入cog
	parts = list(filepath.parts)
	parts[-1] = filepath.stem
	bot.load_extension(".".join(parts))
	logging.debug(f'已載入 {parts} 模塊')

bot.load_extension('admin_cog') # 載入基礎管理用指令cog

if __name__ == "__main__":
	config = get_Json('config')
	if config['token']:
		run_bot()
	else:
		tokenInput()
		run_bot()
