import discord
from discord.ext import commands
import random

"""
這個cog包含了女僕有的功能
"""



class Rice_maid(commands.Cog):
    def __init__(self, bot): 
        self.bot = bot


        
    @discord.slash_command(name="ping")
    async def _ping(self, ctx):
        await ctx.respond(f"目前ping值為 {round(self.bot.latency * 1000)} ms")


    
    @discord.slash_command(name="random")
    async def _random(self, ctx,
                    最大值: discord.Option(int, min_value=-1000, max_value=1000), # type: ignore
                    最小值: discord.Option(int, min_value=-1000, max_value=1000), # type: ignore
                    times: discord.Option(int, name="抽幾次", min_value=1, max_value=10, default=1)): # type: ignore
        rand = {}
        if 最大值 > 最小值:
            max = 最大值
            min = 最小值
        else:
            max = 最小值
            min = 最大值

        rand[max] = max
        rand[min] = min
        rand[times] = times
        
        if max - min < times:
         await ctx.send("範圍過小，無法抽取")
         return

        def ran(min, max, times):
            number = random.sample(range(min, max), times)
            number.sort()
            result = " , ".join(map(str, number))
            embed=discord.Embed(title='以下為隨機結果', description=result,color=discord.Colour.random())
            embed.set_footer(text=f"抽籤數 {times} 最大值{max} 最小值{min}")
            return embed
        
        class rdbutton(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
            @discord.ui.button(label="再抽一次", style=discord.ButtonStyle.primary) 
            async def button_callback(self, button, interaction):
                await interaction.response.edit_message(embed=ran(rand[min], rand[max], rand[times]), view=rdbutton())

        await ctx.respond(embed=ran(rand[min], rand[max], rand[times]), view=rdbutton())



def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Rice_maid(bot)) # add the cog to the bot