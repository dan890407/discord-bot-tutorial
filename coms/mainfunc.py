import discord
from discord.ext import commands

class mainfunc(commands.Cog):

    def __init__(self,bot) -> None:
        self.bot=bot

    @commands.command()
    async def load(self,ctx,extension):
        if extension!="slash":
            await self.bot.load_extension(f"coms.{extension}")
        else:
            await self.bot.load_extension(f"slash.slash")
        await ctx.send(f"load {extension}")

    @commands.command()
    async def unload(self,ctx,extension):
        if extension!="slash":
            await self.bot.unload_extension(f"coms.{extension}")
        else:
            await self.bot.unload_extension(f"slash.slash")
        await ctx.send(f"unload {extension}")

    @commands.command()
    async def reload(self,ctx,extension):
        if extension!="slash":
            await self.bot.reload_extension(f"coms.{extension}")
        else:
            await self.bot.reload_extension(f"slash.slash")
        await ctx.send(f"reload {extension}")

async def setup(bot):
    await bot.add_cog(mainfunc(bot))