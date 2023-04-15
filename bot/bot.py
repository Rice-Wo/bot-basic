import discord
from cool import readJson, writeJson, error_window
import tkinter as tk
import atexit
import time
import asyncio


bot = discord.Bot(status=discord.Status.do_not_disturb, intents = discord.Intents().all())

config = readJson('config')

@atexit.register
async def close_bot():
    await bot.close()
    await asyncio.sleep(5)
    print("Cleaning up...")




def error(reason):
  print(reason)
  root = tk.Tk()
  app = error_window(root)
  root.mainloop()


@bot.event
async def on_ready():
  print(f"機器人 {bot.user} 已經上線了")


@bot.command(name='測試用')
async def _test(ctx):
  await ctx.respond('成功')


if __name__ == '__main__':
    try:
      token = config['token']
      bot.run(token)
    except discord.errors.LoginFailure:
      config = readJson('config')
      config['token'] = ""
      writeJson('config', config)
      error('token錯誤，')
      