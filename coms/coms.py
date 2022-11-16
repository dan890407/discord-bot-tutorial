import discord
from discord.ext import commands
from discord.ui import Button, View

class coms(commands.Cog):

    def __init__(self,bot) -> None:
        self.bot=bot

    @commands.command()
    async def yo(self,ctx):
        await ctx.send("yo man")

    @commands.command()
    async def boo(self,ctx,*,a):
        await ctx.send(f"boo {a}")

    @commands.group()
    async def heyyo(self,ctx):
        await ctx.send("good morning")
    @heyyo.command()
    async def teacher(self,ctx,name):
        await ctx.send(f"professor {name}")
    @heyyo.command()
    async def student(self,ctx,name):
        await ctx.send(f"{name} you have paper to read")

    @commands.command()
    async def sendembed(self,ctx):
        embed=discord.Embed(title="our Lab!", url="https://github.com/UDICatNCHU", description="NCHU NLP", color=0x00d5ff)
        embed.set_image(url="https://cloudfront-us-east-1.images.arcpublishing.com/coindesk/CPBTOUCWKBA4NCNBBRWCRL4HNA.jpg")
        embed.add_field(name="老師", value="范耀中", inline=True)
        embed.add_field(name="大學長", value="余翰承", inline=True)
        view=View()
        view.add_item(Button(label="github1",style=discord.ButtonStyle.link,url="https://github.com/UDICatNCHU"))
        view.add_item(Button(label="github2",style=discord.ButtonStyle.link,url="https://github.com/UDICatNCHU"))
        view.add_item(Button(label="github3",style=discord.ButtonStyle.link,url="https://github.com/UDICatNCHU"))
        await ctx.send(embed=embed,view=view)

    @commands.command()
    async def show_btn(self,ctx):
        view=View()

        bt1=Button(label=":)",style=discord.ButtonStyle.green)
        async def btncall_1(interaction:discord.Interaction):
            await interaction.response.send_message("you can graduate !")
        bt1.callback=btncall_1

        bt2=Button(label=":(",style=discord.ButtonStyle.red)
        async def btncall_2(interaction:discord.Interaction):
            await interaction.response.send_message("you cannot graduate :(")
        bt2.callback=btncall_2

        view.add_item(bt1)
        view.add_item(bt2)
        await ctx.send(view=view)

async def setup(bot):
    await bot.add_cog(coms(bot))


