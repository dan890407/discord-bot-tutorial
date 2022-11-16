
from discord.ext import commands,tasks

class auto_func(commands.Cog):

    def __init__(self,bot):
        self.bot=bot
        self.loopname="looping"

    @tasks.loop(seconds=5)
    async def looping(self):
        print("i am looping")
        await self.channel.send(self.loopname)

    @looping.before_loop
    async def before_looping(self):
        print('waiting...')
        await self.bot.wait_until_ready()
        self.channel=self.bot.get_channel(1024750975522709574)

    @looping.after_loop
    async def after_looping(self):
        await self.channel.send("stop looping")

    @commands.command()
    async def stop_looping(self,ctx):
        self.looping.stop()

    @commands.command()
    async def start_looping(self,ctx):
        self.looping.start()
        print("start looping")

    @commands.command()
    async def set_loopname(self,ctx,name):
        self.loopname=name
        await ctx.send(f"change loop name to {name}")


async def setup(bot):
    await bot.add_cog(auto_func(bot))