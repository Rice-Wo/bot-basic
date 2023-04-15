import discord
from cool import readJson, writeJson


bot = discord.Bot(status=discord.Status.do_not_disturb, intents = discord.Intents().all())

config = readJson('config')




@bot.event
async def on_ready():
  print(f"機器人 {bot.user} 已經上線了")
