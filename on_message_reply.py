import math
import discord
import discord, datetime, time
from discord.ext import commands
from discord.utils import get
import random
from random import randint

from discord.ext.commands import cooldown
from discord.ext.commands import BucketType
from discord.ext import tasks
from bs4 import BeautifulSoup
from discord.ext.commands import Bot

import asyncio
from async_timeout import timeout

adminid = [784335155476037652, 682814885713018924, 301146278656606210, 730624156697362484]

"""
@commands.Cog.listener(name="on_member_join")
async def send_rules_dm_on_join(self, member):
"""

class on_message_reply(commands.Cog):
		def __init__(self, client):
			client.bot = client
	
		@commands.Cog.listener(name="on_message")
		async def _burn(self,message):
			if message.author.bot:
				return
			if "uwu" in message.content.lower():
				await message.channel.send("https://media.giphy.com/media/May0SdjFNSrckK7LO9/giphy.gif")

		@commands.Cog.listener(name="on_message")
		async def _pet(self,message):
		    if message.author.bot:
		        return
		    if "pat" in message.content.lower():
		        await message.channel.send("e")

		@commands.Cog.listener(name="on_message")
		async def _sus(self,message):
		    if message.author.bot:
		        return
		    if "tableflip" in message.content.lower():
		        await message.channel.send
		        ("AHHHHHHHHHH YYYYY U FLIP DA TABLE PUT IT BACK U ASSHOLE")

		@commands.Cog.listener(name="on_message")
		async def _thick(self,message):
		    if message.author.bot:
		        return
		    if "thiccc" in message.content.lower():
		        await message.channel.send("mega slurp")
		    if "thicc" in message.content.lower():
		        await message.channel.send("slurp")				
		
		@commands.Cog.listener(name="on_message")
		async def _fair(self,message):
				if message.author.bot:
						return
				if "fair" in message.content.lower():
						await message.channel.send("fair")
				if "pog" in message.content.lower():
						await message.channel.send("pog")

		@commands.Cog.listener(name="on_message")
		async def _end(self,message):
		    if message.author.bot:
		        return
		    if "i will end you" in message.content.lower() and message.author.id in adminid:
		        await message.channel.send("please dont end me :(")
		    if "i will end u" in message.content.lower() and message.author.id in adminid:
		        await message.channel.send("please dont end me :(")

		@commands.Cog.listener(name="on_message")
		async def _Da(self,message):
		    if message.author.bot:
		        return
		    if "rawr" in message.content.lower():
		        await message.channel.send("Rawr XD")

		@commands.Cog.listener(name="on_message")
		async def _monke(self,message):
		    if message.author.bot:
		        return
		    if "<@784335155476037652>" in message.content:
		        await message.channel.send("Lmao dahud got pinged")
		    if "<@!784335155476037652>" in message.content:
		        await message.channel.send("Lmao dahud got pinged")
		    if "<@!794131697225695274>" in message.content:
		        await message.channel.send("Lmao dino 322 got pinged")
		    if "<@794131697225695274>" in message.content:
		        await message.channel.send("Lmao dino 322 got pinged")
		
		
		@commands.Cog.listener(name="on_message")
		async def _monk(self,message):
		    if message.author.bot:
		        return
		    if "<@744074834933448797>" in message.content:
		        await message.channel.reply("stfu")
		    if "<@!744074834933448797>" in message.content:
		        await message.channel.reply("stfu")

		@commands.Cog.listener(name="on_message")
		async def _plug(self,message):
		    if message.author.bot:
		        return
		    if "plug" in message.content.lower():
		        await message.channel.send("https://discord.gg/BA25fm8E9d")

		@commands.Cog.listener(name="on_message")
		async def _huh(self,message):
		    if message.author.bot:
		        return
		    if "awesomebot" in message.content:
		        await message.content.send
		        ("huh")
		    if "Awesomebot" in message.content:
		        await message.content.send
		        ("huh")

		@commands.Cog.listener(name="on_message")
		async def _e(self,message):
		    if message.author.bot:
		        return
		    if message.author.id in adminid and "<@!802796198947586058>" in message.content:
		        await message.channel.send("Daddy :)")
		    if message.author.id in adminid and "<@802796198947586058>" in message.content:
		        await message.channel.send("Daddy :)")
		    if message.author.id not in adminid and "<@!802796198947586058>" in message.content: 
		            await message.channel.send("stfu mf lookin bish")
		    if message.author.id not in adminid and "<@802796198947586058>" in message.content: 
		            await message.channel.send("stfu mf lookin bish")

