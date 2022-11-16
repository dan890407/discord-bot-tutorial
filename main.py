import os
import json

import discord
from discord.ext import commands


with open("attr.json","r") as f:
    setups=json.load(f)


bot=commands.Bot(command_prefix='!',intents=discord.Intents.all(),appication_id=1033722790232211587)


import asyncio
async def main():

    for cogs in  os.listdir("./coms"):
        if cogs.endswith("py"):
            await bot.load_extension(f"coms.{os.path.splitext(cogs)[0]}")

    await bot.start(setups["token"])

if __name__=="__main__":
    asyncio.run(main())