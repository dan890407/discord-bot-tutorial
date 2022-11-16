# Discord tutorial
get the official [**API**](https://discordpy.readthedocs.io/en/latest/api.html)
##  Pre-work
- register an app on [discord developer portal](https://discord.com/developers/applications )
- get Tokens from your bot
- create an invite link to add the bot to your server :
     >check the checkbox of "bot" in SCOPES

     >set bot permission to administrator
     
     >click on the link to invite bot to server

- set the Privileged Gateway intents to on if you need that intents


## Get your bot online in two ways
### 1. simple way
>bot.run( ) is none async funtion
```python
import discord
from discord.ext import commands

intents=discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

if __name__=="__main__":
    bot.run("your bot token")

```
### 2. with asyncio ( can scale the bot with Cog module)
>bot.start( ) is an async function

```python
import discord
from discord.ext import commands

intents=discord.Intents.all()                           #set intents
bot = commands.Bot(command_prefix='!',intents=intents)  #create bot

import asyncio

async def main():
    await bot.start("your bot token")

if __name__=="__main__":
    asyncio.run(main())

```
*1. personaly recommand **NOT** using bot=discord.Client() , because it's not the newest method* 
*2. It is better to put your bot token in a json file as the code in the repositary*

## Cog 
There comes a point in your bot’s development when you want to organize a collection of commands, listeners, and some state into one class. Cogs allow you to do just that.

* cog is an extension to scale your bot
* when using Cog , make sure to use the second way as the above to run bot with asyncio
- useful in debugging your program
- It's better to put your Cogs in a directory (use "coms" as directory name as example)

**Basic Cog template :**
```python
import discord
from discord.ext import commands

class yourCog(commands.Cog):
	def __init__(self,bot) -> None:
		self.bot=bot
		
	"""
		
	your function
		
	"""
	
async def setup(bot):
    await bot.add_cog(yourCog(bot))
```
setup( ) allows the bot to set the Cog when the Cog file loaded
*# note that add_cog is a coroutine*

**Things to add in the main python file**
```python
import asyncio
async def main():

    for cogs in  os.listdir("./coms"):
        if cogs.endswith("py"):
            await bot.load_extension(f"coms.{os.path.splitext(cogs)[0]}")

    await bot.start("your bot token")

if __name__=="__main__":
    asyncio.run(main())
```

*note that bot.load( ) is a coroutine function , so it must be written in the form of async function*

## Text Command

difference in decorater between using Cog or not
| no Cog | Cog | 
| -------- | -------- | 
| @bot.command     | @commands.command | 

#### 1. no Cog
```python
@bot.command()
async def your_command_name(ctx):
	await ctx.send("something")
```
#### 2. Cog
```python
import discord
from discord.ext import commands

class yourCog(commands.Cog):
	def __init__(self,bot) -> None:
		self.bot=bot
		
	@commands.command()
	async def your_command_name(ctx):
		await ctx.send("something")
	
		
async def setup(bot):
    await bot.add_cog(yourCog(bot))
```
### set parameters to positional only to allow spaces in input
```python
@commands.command()
async def boo(self,ctx,*,context_with_spaces):
    await ctx.send(context_with_spaces)
```
### Basic commands to debug Cog

```python
import discord
from discord.ext import commands

class yourCog(commands.Cog):
	def __init__(self,bot) -> None:
		self.bot=bot
	
	@commands.command()
	async def load(self,ctx,extension):
		await self.bot.load_extension(f"coms.{extension}")
		await ctx.send(f"load {extension}")
	
	@commands.command()
	async def unload(self,ctx,extension):
		await self.bot.unload_extension(f"coms.{extension}")
		await ctx.send(f"unload {extension}")

	@commands.command()
	async def reload(self,ctx,extension):
		await self.bot.reload_extension(f"coms.{extension}")
		await ctx.send(f"reload {extension}")
	
async def setup(bot):
    await bot.add_cog(yourCog(bot))
```
### group commands
```python
@commands.group()
async def heyyo(self,ctx):
    await ctx.send("good morning")
@heyyo.command()
async def teacher(self,ctx,name):
    await ctx.send(f"teacher {name}")
@heyyo.command()
async def student(self,ctx,name):
    await ctx.send(f"student {name}")
```
## Event Calls
* call when a specific incident happens
* all built-in event name can be found in official API

| no Cog | Cog | 
| -------- | -------- | 
| @bot.event or @bot.listen()|@commands.Cog.listener() |

#### @bot.event
```python
@bot.event
async def on_message(message):		#call when receive a message
    if message.author == bot.user:	#prevent bot listen to own message
        return
    if "hi" in message.content :	 
        await message.channel.send('hi')
    await bot.process_commands(message)  #add this if you overide the on_message()
```

#### @bot.listen( )
```python=
@bot.listen('on_message')
async def name_whatever_you_want(message):
    if message.author == bot.user:
        return
    if "hi" in message.content :
        await message.channel.send('hi') 
```

#### @commands.Cog.listener()
```python
import discord
from discord.ext import commands

class yourCog(commands.Cog):
	def __init__(self,bot) -> None:
		self.bot=bot
		
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        if "hi" in message.content :
            await message.channel.send('hi')
		
async def setup(bot):
    await bot.add_cog(yourCog(bot))
```
## Background functions
use @task.loop to create a back ground function executes every 5 seconds
```python
from discord.ext import commands,tasks

class auto_func(commands.Cog):

    def __init__(self,bot):
        self.bot=bot
        self.loopname="looping"

    @tasks.loop(seconds=5)
    async def looping(self):
        await self.channel.send("i am looping")

    @looping.before_loop
    async def before_looping(self):
        await self.bot.wait_until_ready()
        self.channel=self.bot.get_channel("your channel id")


async def setup(bot):
    await bot.add_cog(auto_func(bot))
```

## Slash commands
* slash commmands is an another way to input command , the prefix are always be "/" , after you enter "/" , a pop up option will appear on top of the input textbox 
* slash commands can customize the input title , description, etc.

```python
import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice

class slash(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot=bot


    @app_commands.command(name="slash command",description="my slash command")
    @app_commands.describe(user="name",activity="activity")
    @app_commands.choices(activity=[Choice(name="basketball",value="ball"),
                               Choice(name="tabel tennis",value="ball"),
                               Choice(name="coding",value="computer")])
    async def nlpapi(self, interaction:discord.Interaction, user:str, activity:Choice[str]):
        await interaction.response.send_message(f" {user} love {activity.name} !")

    @commands.command()
    async def slash_load_succesful(self,ctx):
        await ctx.send("succes")

async def setup(bot):
    await bot.add_cog(slash(bot))
```
## Discord Interactions
discord Interaction module allow bot to send embeds, pop up forms,many kinds of interactable interfaces,etc.
* use **discord.ui.View()** to create a basic view . View act like a template.
* Any other things wants to show in the message can added to the view to be sent
### embeded messages
```python
from discord.ext import commands
from discord.ui import Button, View

class coms(commands.Cog):

    def __init__(self,bot) -> None:
        self.bot=bot
	@commands.command()
    async def sendembed(self,ctx):
        embed=discord.Embed(title="title", url="www.google.com", description="description", color=0x00d5ff)
        embed.set_image(url="www.your_image_url.com")
        embed.add_field(name="name1", value="name1", inline=True)
        embed.add_field(name="name2", value="name2", inline=True)
		await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(coms(bot))
```
### Buttons
need View to visualize
```python
from discord.ext import commands
from discord.ui import Button, View

class btn(commands.Cog):

    def __init__(self,bot) -> None:
        self.bot=bot
	
	@commands.command()
    async def show_btn(self,ctx):
        view=View()										#create View

        bt1=Button(label=":)",style=discord.ButtonStyle.green)
        async def btncall_1(interaction:discord.Interaction):
            await interaction.response.send_message("you can graduate !")
        bt1.callback=btncall_1                       	#bind function to the button 

        bt2=Button(label=":(",style=discord.ButtonStyle.red)
        async def btncall_2(interaction:discord.Interaction):
            await interaction.response.send_message("you cannot graduate :(")
        bt2.callback=btncall_2							#bind function to the button 

        view.add_item(bt1)
        view.add_item(bt2)								#add button to View
        await ctx.send(view=view)

async def setup(bot):
    await bot.add_cog(btn(bot))
```


### see the official API for more information of other discord bot function
