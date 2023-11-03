import discord
from discord.ext import commands
import random

"""
這個cog包含了女僕有的功能
"""



class Rice_maid(commands.Cog):
    def __init__(self, bot): 
        self.bot = bot


        
   


    
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


    @discord.slash_command(name="choice",description="幫你從兩個到五個選項中選一個")
    async def _choice(self, ctx,
                    ques: discord.Option(str,"問題是什麼", name="問題"), # type: ignore
                    times: discord.Option(int, name="選項數", min_value=2, max_value=5, default=2)): # type: ignore
        list = []

        def ci(self, interaction: discord.Interaction):
        
            for j in range(len(self.children)):
                value = self.children[j].value
                list.append(value)
            return list

        def rc(ques, list):
            select = " ".join(list)  
            embed=discord.Embed(title=f"關於 {ques} ", color = discord.Colour.random())
            embed.add_field(name=f"{random.choice(list)}", value=f"從 {select} 裡面選一個出來的", inline=False)
            embed.set_footer(text="本結果為隨機選出，僅供參考")
            return embed 
        
        class rcbutton(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
            @discord.ui.button(label="再選一次", style=discord.ButtonStyle.primary)
            async def button_callback(self, button, interaction):
              await interaction.response.edit_message(embed=rc(ques, list), view=rcbutton())

        class cimodal(discord.ui.Modal):
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(*args, **kwargs)

                for i in range(0, times):
                   self.add_item(discord.ui.InputText(label=f"第 {i+1} 個選項"))        

            async def callback(self, interaction: discord.Interaction):
                await interaction.response.send_message(embed=rc(ques, ci(self, interaction)), view=rcbutton())

        class cibutton(discord.ui.View):
            @discord.ui.button(label="按這填入選項")
            async def button_callback(self, button, interaction):
                await interaction.response.send_modal(cimodal(title="請輸入選項"))
        
        await ctx.respond(view=cibutton())




def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Rice_maid(bot)) # add the cog to the bot