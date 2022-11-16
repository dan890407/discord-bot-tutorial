import discord
from discord.ext import commands



class bot_events(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.load_extension("slash.slash")
        await self.bot.tree.sync()
        print("bot is running")

    """@commands.Cog.listener()
    async def on_message_delete(self,message):
        if message.author == self.bot.user:
            return
        else:
            return
            #await message.channel.send(f'Anti delete:\n{message.author.display_name} : {message.content}')


    @commands.Cog.listener()
    async def on_message_edit(self,before, after):
        if before.author == self.bot.user:
            return
        else:
            return
            #await before.channel.send(f"Anti edit:\n{before.author.display_name} : {before.content}")"""

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        if "hi" in message.content :
            await message.channel.send(f'hi {message.author}')
        #not need await self.bot.process_commands(message)  in extensions

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload:discord.RawReactionActionEvent):
        guild=self.bot.get_guild(payload.guild_id)
        if payload.message_id==1035454344964870205:
            print("yes")
            if payload.emoji==discord.PartialEmoji(name='🐒'):
                print(f"{payload.member} get monkey role" )
                await payload.member.add_roles(guild.get_role(1035455100086399007))
            if payload.emoji==discord.PartialEmoji(name='🐱'):
                print(f"{payload.member} get cat role" )
                await payload.member.add_roles(guild.get_role(1035455273013354497))
            if payload.emoji==discord.PartialEmoji(name='🐷'):
                print(f"{payload.member} get pig role" )
                await payload.member.add_roles(guild.get_role(1035455149210075146))
            if payload.emoji==discord.PartialEmoji(name='😡'):
                print(f"{guild.get_member(payload.user_id)} remove rage role")
                await payload.member.add_roles(guild.get_role(1035470757075099688))

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload:discord.RawReactionActionEvent):
        guild=self.bot.get_guild(payload.guild_id)
        user=guild.get_member(payload.user_id)
        if payload.message_id==1035454344964870205:
            print("re")
            if user is not None:
                if payload.emoji==discord.PartialEmoji(name='🐒'):
                    print(f"{guild.get_member(payload.user_id)} remove monkey role")
                    await user.remove_roles(guild.get_role(1035455100086399007))
                if payload.emoji==discord.PartialEmoji(name='🐱'):
                    print(f"{guild.get_member(payload.user_id)} remove cat role")
                    await user.remove_roles(guild.get_role(1035455273013354497))
                if payload.emoji==discord.PartialEmoji(name='🐷'):
                    print(f"{guild.get_member(payload.user_id)} remove pig role")
                    await user.remove_roles(guild.get_role(1035455149210075146))
                if payload.emoji==discord.PartialEmoji(name='😡'):
                    print(f"{guild.get_member(payload.user_id)} remove rage role")
                    await user.remove_roles(guild.get_role(1035470757075099688))
            else:
                print("no user")

async def setup(bot):
    await bot.add_cog(bot_events(bot))