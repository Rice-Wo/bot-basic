import tkinter as tk
import os
import logging
from fun import readJson, writeJson
import discord
from windows import error_window
from pathlib import Path
from discord.ext import commands
from datetime import datetime


#設定日誌
logs_folder = "logs"
os.makedirs(logs_folder, exist_ok=True)

current_time = datetime.now()
log_filename = f"error_{current_time.strftime('%Y%m%d_%H%M%S')}.log"
log_path = os.path.join(logs_folder, log_filename)

logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s [%(levelname)s] : %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
)




#discord 機器人
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(status=discord.Status.do_not_disturb, intents = intents)




@bot.event
async def on_ready():
	logging.info(f"機器人 {bot.user} 已經上線了")
	logging.info('請勿關閉本視窗以維持機器人上線狀態，可以最小化')
	logging.info('如要關閉機器人請使用/close 或者在本視窗按下ctrl+C')


@bot.command(name='close')
@commands.is_owner()
async def _close(ctx):
	await ctx.response('正在關閉機器人')
	await bot.close()

@_close.error
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
    if isinstance(error, commands.NotOwner):
        await ctx.respond("只有機器人主人能使用這個指令!")
    else:
        raise error






if not os.path.exists("config.json"):    
	# 創建一個新的設定檔
	config = {
		'token': "",
		'setting2': 'value2',
		'setting3': 'value3'
	}
	writeJson('config', config)
	config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
	logging.debug(f'已創建config.json，檔案位置 {config_file}')


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
	config = readJson('config')
	try:
		token = config['token']
		bot.run(token)
	except discord.errors.LoginFailure:
		config['token'] = ""
		writeJson('config', config)
		error('token錯誤或過期，請重新輸入')
	except Exception as e:
		error(e)

for filepath in Path("./cogs").glob("**/*.py"):
	cog_name = Path(filepath).stem
	bot.load_extension(f"cogs.{cog_name}")

if __name__ == "__main__":
	config = readJson('config')
	if config['token']:
		run_bot()
	else:
		tokenInput()
		run_bot()
