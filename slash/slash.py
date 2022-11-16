import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice

class slash(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot=bot


    @app_commands.command(name="nlpapi",description="our labs api!")
    @app_commands.describe(user="name",activity="activity")
    @app_commands.choices(activity=[Choice(name="basketball",value="odqa"),
                               Choice(name="tabel tennis",value="QA"),
                               Choice(name="coding",value="QG")])
    async def nlpapi(self, interaction:discord.Interaction, user:str, activity:Choice[str]):
        await interaction.response.send_message(f" {user} love {activity.name} !")

    @commands.command()
    async def slash_load_succesful(self,ctx):
        await ctx.send("succes")

async def setup(bot):
    await bot.add_cog(slash(bot))