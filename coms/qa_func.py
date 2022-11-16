# -*- encoding: utf-8 -*-
import discord
from discord.ext import commands
from transformers import pipeline

class qa_func(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot=bot

    @commands.command()
    async def qa(self,ctx,question,*,context):
        classifier = pipeline("question-answering",model = "HankyStyle/Question-Answering-for-Argriculture")
        res = classifier(question=question,context=context)
        print(res['answer'])
        await ctx.send(res['answer'])

async def setup(bot):
    await bot.add_cog(qa_func(bot))