import discord
from discord.ext import commands
import requests
from lxml import html
import re
import json
from bs4 import BeautifulSoup, SoupStrainer
import asyncio
from time import sleep

prefix = "!"
cleanup = True

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Bot is online")
    game = discord.Game("!<command>")
    await bot.change_presence(activity=game)

    while(True):
        response = requests.get('https://twitter.com/search?q=zoom.us%2Fj%2F&src=typed_query&f=live')

        links = re.findall('https?://[^\s]+', response.content.decode())
        print(links)
        sleep(5)

@bot.event
async def on_guild_join(guild):
    await guild.create_text_channel("zoom-links")
    await guild.create_text_channel("meet-links")

async def send_results():
    pass





bot.run("Your_Discord_Token_Here")

