# discord-bot-tutorial
##  Pre-work
- register an app on [discord developer portal](https://discord.com/developers/applications )
- get Tokens from your bot
- create an invite link to add the bot to your server :
     >check the checkbox of "bot" in SCOPES

     >set bot permission to administrator
     
     >click on the link to invite bot to server


## Get your bot online in two ways
### 1. simple way
```python
import discord
from discord.ext import commands

intents=discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

if __name__=="__main__":
    bot.run("your bot token")

```
### 2. with asyncio ( can scale the bot with Cog module)

```python
import discord
from discord.ext import commands

intents=discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

import asyncio

async def main():
    await bot.start("your bot token")

if __name__=="__main__":
    asyncio.run(main())

```

