import discord
from discord.ext import commands
import random

"""
所有跟機器人最基本功能有關聯的都在這
"""



class system(commands.Cog):
    def __init__(self, bot): 
        self.bot = bot


        
    @discord.slash_command(name="ping")
    async def _ping(self, ctx):
        await ctx.respond(f"目前ping值為 {round(self.bot.latency * 1000)} ms")

    @discord.slash_command(name='close')
    @commands.is_owner()
    async def _close(self, ctx):
        await ctx.respond('正在關閉機器人')
        await self.bot.close()
        
    
    
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.NotOwner):
            await ctx.send("只有機器人主人能使用這個指令!")
        else:
            raise error  # Here we raise other errors to ensure they aren't ignored



def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(system(bot)) # add the cog to the bot