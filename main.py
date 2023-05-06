import tkinter as tk
import os
import logging
from fun import readJson, writeJson
import discord
from windows import error_window

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')



bot = discord.Bot(status=discord.Status.do_not_disturb, intents = discord.Intents().all())


if os.path.exists("config.json"):    
		pass
else:
	# 創建一個新的設定檔
	config = {
		'token': "",
		'setting2': 'value2',
		'setting3': 'value3'
	}
	writeJson('config', config)
config = readJson('config')


@bot.event
async def on_ready():
  print(f"機器人 {bot.user} 已經上線了")


@bot.command(name='測試用')
async def _test(ctx):
  await ctx.respond('成功')











def error(reason):
	logging.critical(reason)
	root = tk.Tk()
	app = error_window(root, reason)
	root.mainloop()

def tokenInput():
	T = input('請輸入token')
	config = readJson('config')
	config['token'] = T
	writeJson('config', config)


def run_bot():
	try:
		token = config['token']
		bot.run(token)
	except discord.errors.LoginFailure:
		config['token'] = ""
		writeJson('config', config)
		error('token錯誤或過期，請重新輸入')
	except Exception as e:
		error(e)


if __name__ == "__main__":

	


	config = readJson('config')
	if config['token']:
		run_bot()
	else:
		tokenInput()
		run_bot()
