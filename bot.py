#Namelesscreators bot

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = command.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print ("The NamelessCreators bot is ready")
    print ("Im running on" + bot.user.name)

    bot.run("TOKEN HIER")
