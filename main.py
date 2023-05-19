import tkinter as tk
import os
import logging
from fun import readJson, writeJson
import discord
from windows import error_window
from pathlib import Path
from discord.ext import commands



logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(status=discord.Status.do_not_disturb, intents = intents)


if not os.path.exists("config.json"):    
	# 創建一個新的設定檔
	config = {
		'token': "",
		'setting2': 'value2',
		'setting3': 'value3'
	}
	writeJson('config', config)

@bot.event
async def on_ready():
  logging.info(f"機器人 {bot.user} 已經上線了")


@bot.command(name='close')
@commands.is_owner()
async def _close(ctx):
  await ctx.response('正在關閉機器人', el)
  await bot.close()

@_close.error
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
    if isinstance(error, commands.NotOwner):
        await ctx.respond("只有機器人主人能使用這個指令!")
    else:
        raise error









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
