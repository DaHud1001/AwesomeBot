'''
Copyright (©) 2022 Hudson Hultberg-Espinoza <hudson.espinoza07@gmail.com>
This software/program has a copyright license, more `   information is in the 'LICENSE' file
IF YOU WANT TO USE/COPY/MODIFY/REPRODUCE/RE-DISTRIBUTE THIS PROGRAM, YOU MUST INCLUDE A COPY OF THE LICENSE

'plsworkalty@outlook.com'
Author Name: Hudson Hultberg-Espinoza, Kiet Pham
Author Contact: hudson.espinoza07@gmail.com
Discord: DaHud1001#2668 (prefered contact)
Discord Server: https://discord.gg/BA25fm8E9d
Original Github: https://github.com/CaptainVietnam6


Program Status: ACTIVE
'''
import math
import discord
import discord, datetime, time
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
import os
from os import system
import random
from random import randint
import time
import asyncio
import youtube_dl
from keep_alive import keep_alive
#from BOT_TOKEN import BOT_TOKEN
from itertools import cycle
from discord.ext.commands import cooldown
from discord.ext.commands import BucketType
from discord import FFmpegPCMAudio
from discord.ext import tasks
from bs4 import BeautifulSoup
from discord.ext.commands import Bot
#other important imports for system
import shutil
import asyncio
import PyDictionary
from PyDictionary import PyDictionary
import itertools
import sys
import traceback
import json
#import MemeFeedBot.mp4 
from discord.ui import Button, View, Select
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL
import datetime
import humanfriendly
bot_prefixes = ["bot", "bot ","/", "/ " , "*" ,"* ", "awesomebot " , "awesomebot" , "Awesomebot" , "Awesomebot "]
client = commands.Bot(command_prefix=bot_prefixes,help_command=None)

import on_message_reply
from on_message_reply import on_message_reply
client.add_cog(on_message_reply(client))

'ytdl = YoutubeDL(ytdlopts)'
Version = "Version Beta 1.5"
Versiondesc = "Revamped Help Menu V2"
print (f"Currently In {Version}, {Versiondesc}.")

colours = [0xCC0000, 0x33BAFB, 0x00ff44, 0x770026, 0xD6B2BD, 0xFFFF00, 0x0000FF, 0x999999, 0x800080]

#my id first
adminid = [784335155476037652, 682814885713018924, 301146278656606210, 730624156697362484, 784026648357371904,1010769795630768158]
#I forgor to add you lmao
nouse = [852982931969278002, 691359367429095514]

onlydahud = [784335155476037652, 1010769795630768158]

spamtyp = {}

class spam:
	loop = False

def loadJsonData(name):
    global config
    if os.path.exists(name+".json"):
        with open("{}.json".format(name), "r") as f:
            config = json.load(f)
    else:
        with open("{}.json".format(name), "w") as f:
            f.write("{\"users\": []}")
            f.close()
        with open("{}.json".format(name), "r") as f:
            config = json.load(f)

def saveConfig(name):
    with open("{}.json".format(name), "w") as f:
        json.dump(config, f, indent=4)

bot_prefixes = ["bot", "bot ","/", "/ " , "*" ,"* ", "awesomebot " , "awesomebot" , "Awesomebot" , "Awesomebot "]


#client.remove_command("help")
token = os.environ.get("BOT_TOKEN")

@client.event
async def on_ready():
	changestatus.start()
	time.sleep(3)
	print("AwesomeBot is ready")


'''
@client.listen("on_message")
async def config(message):
	config = 0
	if config == 0:
		await client.process_commands(message)
		config += 1
'''
'''@client.listen(name="on_message")
async def _replynumber(self,message,number):
    number = author.messsage
		if message.author.bot and numb:
		    return
		if "" in message.content:
		    await message.channel.reply("stfu")
		if "<@!744074834933448797>" in message.content:
		    await message.channel.reply("stfu")'''

@client.command(aliases=["reply", "Reply"])
async def replycommand(ctx, messag, emoji):
    messag = int(messag)
    messag = await ctx.fetch_message(messag)
    await messag.add_reaction(emoji)
    if ctx.author.id in adminid:
        try:
            await messag.message.add_reaction(f"{emoji}")
        except:
            messag = int(messag)
            messag = await ctx.fetch_message(messag)
            await messag.add_reaction(emoji)
    


@tasks.loop(seconds=60)
async def changestatus():
	serveramount = str(len(client.guilds))
	status = ["Sniffing People in " + serveramount + " servers!", 
            "*help"]

	for i in status:
		await client.change_presence(activity=discord.Game(i))
		await asyncio.sleep(60)

#admin  
@client.command()
async def thack(ctx, user: discord.Member=None, time=None, *, reason=None):
    time = humanfriendly.parse_timespan(time)
    await user.timeout(until = discord.utils.utcnow() +datetime.timedelta(seconds=time), reason=reason)
    await ctx.send(f"{user} has been timed out for {time}, Reason: {reason}")

@client.command()
async def nhack(ctx, user: discord.Member=None, *, reason=None):
    await user.timeout(until=None, reason=reason)
    await ctx.send(f"Timeout Removed From {user}")
    
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason=" no reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f'User {member.mention} has been kicked for {reason}')

@client.command()
async def khack(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason=" no reason provided"
    await ctx.guild.kick(member)

@client.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason=" no reason provided"
    await ctx.guild.ban(member)
    await ctx.send(f'User {member.mention} has been banned for {reason} lmao')

@client.command()
async def bhack(ctx, member: discord.Member, *, reason=None):
    if ctx.author.id in adminid:
        if reason==None:
          reason=" no reason provided"
        await ctx.guild.ban(member)

@ban.error
async def _chat_clear(ctx, error):
	if isinstance(error, commands.errors.CommandInvokeError):
		await ctx.reply("I Cannot Ban This User, I May Not Have `Administrator` Permission.")

@kick.error
async def _kickerror(ctx, error):
	if isinstance(error, commands.errors.CommandInvokeError):
		await ctx.reply("I Cannot Kick This User, I May Not Have `Administrator` Permission.")

@khack.error
async def _khackerror(ctx, error):
	if isinstance(error, commands.errors.CommandInvokeError):
		await ctx.reply("I Cannot Kick This User, I May Not Have `Administrator` Permission.")

@bhack.error
async def _bhackerror(ctx, error):
	if isinstance(error, commands.errors.CommandInvokeError):
		await ctx.reply("I Cannot Ban This User, I May Not Have `Administrator` Permission.")


@client.command()
async def rhack(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="18+")
    await client.add_roles(user, role)
    

#COMMAND TO REPLY WITH BOT'S PING OR LATENCY
@client.command(aliases=["ping", "Ping", "latency", "Latency"])
async def _ping(ctx):
    ping = round(client.latency * 1000)
    await ctx.send(f"Pong! my latency is `{ping}ms`")
    await ctx.message.add_reaction('🏓')
    
@client.command(aliases=["playlist", "Playlist"])
async def _playlist(ctx):
    await ctx.send("https://open.spotify.com/playlist/1KTeAu8pQolHssOPuCwl8H")


@client.command(aliases = ["clear", "Clear", "Purge", "purge"])
@commands.has_permissions(manage_messages=True)  
@cooldown(1, 10, BucketType.default)
async def _chat_clear(ctx, amount:int=0):
    await ctx.channel.purge(limit = amount + 1)
    await asyncio.sleep(float(1))
    await ctx.send (f"Cleared {amount} message(s) from chat", delete_after=1)

@_chat_clear.error
async def chatclearerror(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("You are on cooldown")

@client.command(aliases = ["pur", "Pur", "Cle", "cle", "chack", "phack", "Chack", "Phack"])
#@cooldown(1, 10, BucketType.default)
async def my_personal_purge(ctx,*, amount:int=0):
    if ctx.author.id in adminid:
        await ctx.channel.purge(limit = amount + 1)
        await asyncio.sleep(1)
        await ctx.send (f"Cleared {amount} message(s) from chat", delete_after=1)

@my_personal_purge.error
async def mypersonalpurgererror(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("You are on cooldown")

'''class MyView(View):
    @discord.ui.button(label="DaHud is amazing", style=discord.ButtonStyle.primary, emoji="😏")
    async def button(self, button, interaction):
        button.label="Correct"
        button.disabled=True
        await interaction.response.edit_message(view=self)

@client.command()
async def hello(ctx):
    view = MyView()
    await ctx.send("Hi", view=view)
    @client.command()
    async def buttontest(ctx):
        button2 = Button(label="DaHud is amazing")
        button1 = Button(label="DaHud sucks", style=discord.ButtonStyle.red, emoji="😏")
        button3 = Button(label="DaHud is mega pro", style=discord.ButtonStyle.primary, emoji="😏")
        async def button_callback(interaction):
            await interaction.response.send_message("right")
        button2.callback = button_callback    
    async def button1_callback(interaction):
        await interaction.response.send_message("wrong")
        button1.callback = button1_callback
    async def button3_callback(interaction):
        await interaction.response.send_message("right")
        button3.callback = button3_callback    
    view=View()
    view.add_item(button)
    view.add_item(button1)
    view.add_item(button3)
    await ctx.send(view=view)'''

'''@client.command(aliases=["bantest", "Bantest"])
async def bantest(ctx, member: discord.Member):
    select = Select(min_values=1,max_values=1,
        placeholder="Choose a Ban Option",
        options=[
            discord.SelectOption(
                label=f"Ban {member}", 
                description=f"Ban {member} from this guild"
            ),
            discord.SelectOption(
                label=f"Dont Ban {member}", 
                description=f"Keep {member} in this guild"
    )
            
    view=View()
    view.add_item(select)
    embed = await ctx.send("Choose Your Ban Menu <:trollskull:963308954350411776>", view=view)
    
    async def bantestpart2(interaction):
        if select.values[0] == f"Ban {member}" and ctx.author.id in adminid:
            await ctx.guild.ban(member)
        elif select.values[0] == f"Dont Ban {member}"and ctx.author.id in adminid:
            await ctx.send(f"Didnt ban {member}")
        else:
            await ctx.send(You arent a on the bot admin lost)

    select.callback = my_callback'''

@client.command(aliases=["help", "Help"])
async def buttontest(ctx):
    select = Select(min_values=1,max_values=1,
        placeholder="Choose a Help Menu",
        options=[
            discord.SelectOption(
                label="Main Help", 
                description="Main Help Menu"
            ),
            discord.SelectOption(
                label="SoundBoard Help", 
                description="SoundBoard Help Menu"
            ),
            discord.SelectOption(
                label="Admin Help",
                description="Admin Help Menu"
            ),
            discord.SelectOption(
                label="Math Help",
                description="Math Help Menu"
            ),
            discord.SelectOption(
                label="Hacks Menu",
                description="Special Access Hacks Menu"
            )
        ]
    )
    
    author_name = ctx.author.display_name
    helpembed = discord.Embed(
        title = "**Help menu commands <:totem:968199047032754257>:**",
        description = "`*8ball` to get a free response \n `*Dice` to get a random number between 1-12 \n `*Owner` to ping Dahud \n `*Pause` to pause a song \n `*Resume` to resume a song\n `*Repeat` to repeat your message \n `*Dict` (word) to get a link to the words definition \n `*Playlist` for the most poggers playlist\n `*Boobs` (not what you think i promise) \n `*Version` for info in the version \n `*Website` for awesomebots personal website\n `*Snipe` To snipe a message \n `*Embed` for a custom embed (use "" for a message longer than 1 word) \n add `dm` to the end of 'snipe' or 'embed' command to be dm'ed it \n `*Reply 'message id' 'emoji'` for the bot to reply to a message of your choice ",
        color = random.choice(colours)
    )

    author_name1 = ctx.author.display_name
    sbembed = discord.Embed(
        title = "**Soundboard related commands list: 🔊**",
        description = "**Soundboard Help**\n\nJoin VC: **`*join`**\nLeave VC: **`*leave`**\nAirhorn: **`*sb airhorn`**\nAli-a intro: **`*sb alia`**\nBegone thot: **`*sb begonethot`**\nDamn son where'd you find this: **`*sb damnson`**\nDankstorm: **`*sb dankstorm`**\nDeez nuts: **`*sb deeznuts`**\nDeja Vu: **`*sb dejavu`**\nLook at this dude: **`*sb dis_dude`**\nAnother fag left the chat: **`*sb fleft`**\nFart: **`*sb fart`**\nHa gaaayyy: **`*sb hagay`**\nIt's called hentai and it's art: **`*sb henart`**\nIlluminati song: **`*sb illuminati`**\nBitch Lasagna: **`*sb lasagna`**\nLoser: **`*sb loser`**\nNoob: **`*sb noob`**\nOof sound: **`*sb oof`**\nOhGreatHeavens: **`*sb oh greats heavens`**\nPickle Rick: **`*sb picklerick`**\nNice: **`*sb nice`**\nWhy don't we just relax and turn on the radio: **`*sb radio`**\nRick roll: **`*sb rickroll`**\nThis is sparta: **`*sb sparta`**\nTitanic flute fail: **`*sb titanic`**\nGTA V Wasted: **`*sb wasted`**\n **`*Wide Putin` Suprise**\nWubba lubba dub dub: **`*sb wubba`**\n**`*sb yes` Talking Ben Yes**\n**`sb no` Talking Ben No**",
        color = random.choice(colours)
    )

    author_name = ctx.author.display_name
    adminembed = discord.Embed(
        title = "**Admin menu commands 🛠️:**",
        description = "`*ban` to ban someone \n `*kick` to kick someone \n `*purge (number)` to delete messages",
        color = random.choice(colours)
    )

    author_name = ctx.author.display_name
    hackembed = discord.Embed(
        title = "**Hacks menu commands 💻:**",
        description = "`*chack` the Hacks version of \n `*purge` (you must have yourself added by DaHud) \n `*bhack` to ban someone \n `*khack` to kick someone",
        color = random.choice(colours)
    )

    author_name = ctx.author.display_name
    mathembed = discord.Embed(
        title = "**Math menu commands ➕ ➖:**",
        description = "`*add` (Plus Two Numbers (ex: add 1 1)) \n `*subtract` (Two Numbers) \n `*divide` (Two Numbers) \n `*multiply` (Two Numbers) \n `*square` (One Number)",
        color = random.choice(colours)
    )
    
    view = View()
    view.add_item(select)
    embed = await ctx.send("Choose Your Help Menu <:trollskull:963308954350411776>", view=view)
	
    async def my_callback(interaction):
        if interaction.user == ctx.author:
            if select.values[0] == "Main Help":
                helpembed.set_footer(icon_url = ctx.author.avatar,text = f"Requested by {author_name1}\n" + Version)
                await embed.edit(embed=helpembed)
            elif select.values[0] == "SoundBoard Help":
                sbembed.set_footer(icon_url = ctx.author.avatar,text = f"Requested by {author_name1}\n" + Version)
                await embed.edit(embed=sbembed)
            elif select.values[0] == "Admin Help":
                adminembed.set_footer(icon_url = ctx.author.avatar,text = f"Requested by {author_name1}\n" + Version)
                await embed.edit(embed=adminembed)
            elif select.values[0] == "Math Help":
                mathembed.set_footer(icon_url = ctx.author.avatar,text = f"Requested by {author_name1}\n" + Version)
                await embed.edit(embed=mathembed)
            elif select.values[0] == "Hacks Menu":
                if ctx.author.id in adminid:{
									
									hackembed.set_footer(icon_url = ctx.author.avatar,text = f"Requested by {author_name1}\n" + Version),
								  await embed.edit(embed=hackembed)
							}
                else: await interaction.response.send_message("You're not a bot admin <:trollskull:963308954350411776>", ephemeral=True)
        else: await interaction.response.send_message("This is not for you <:trollskull:963308954350411776>", ephemeral=True)

            
    select.callback = my_callback
    
@client.command(aliases = ["Dictionary", "dictionary", "Dict", "dict"])
@cooldown(3, 30, BucketType.default)
async def _dictionarylink(ctx, user_dictionary_request):
    print(f"Someone used the dictionary command for the word {user_dictionary_request}")
    await ctx.send(f"Getting you the dictionary link for the word `{user_dictionary_request}`")
    await asyncio.sleep(float(0.5))
    await ctx.send(f"Here you go! :)\nhttps://www.dictionary.com/browse/{user_dictionary_request}?s=t")

@client.command(aliases = ["wiki", "Wiki", "Wikihow", "wikihow", "Wiki how", "Wiki How"])
@cooldown(3, 30, BucketType.default)
async def _wikihowlink(ctx, user_dictionary_request):
    print(f"someone searched how to {user_dictionary_request}")
    await ctx.send(f"Getting how to `{user_dictionary_request}`") 
    await asyncio.sleep(float(0.5))
    await ctx.send(f"Here you go! :)\nhttps://www.wikihow.com/wikiHowTo?search={user_dictionary_request}")


    
#COMMAND FOR PINGING OWNER UPON .ADMIN
@client.command(aliases=["owner", "Owner", "Dad", "dad"])
async def _owner(ctx):
    await ctx.send("<@784335155476037652>")
    await ctx.message.add_reaction('😠')
    print("someone summoned DaHud")

@client.command(aliases=["loser", "Loser", "Putin", "putin"])
async def _loser(ctx):
    await ctx.send("http://loser.com/")
    await ctx.message.add_reaction('😂')
    print("Sent 'Loser'")

@client.command(aliases=["spam"])
@cooldown(1, 2, BucketType.default)
async def _spamusermessage(ctx, *, user_input):
    await asyncio.sleep(float(0.1))
    print("spam command activated")
    for i in range(3):
        if ctx.author.id in nouse:
            await ctx.repy("You Cant Use This mf LMAO, talk to dahud to get perms back")
        else:
            await ctx.send(f"{user_input}")
            await asyncio.sleep(0.1)
    await ctx.message.add_reaction('💪')			
    print("spam command finished")

async def createacc(guild):
	try:
		spamtyp[guild]
	except KeyError:
		spamtyp[guild] = {
			"loop" : False
		}

@client.command(aliases=["testspam"])
async def test(ctx, *, user_input):
    print("online test activated")
    guild = str(ctx.guild.id)
    await createacc(guild)
    if ctx.author.id in onlydahud or ctx.author.id in adminid and not spamtyp[guild]["loop"]:
        spamtyp[guild]["loop"] = True
        while spamtyp[guild]["loop"]:
            await ctx.send(f"{user_input}")
            await asyncio.sleep(1.5)

    elif spamtyp[guild]["loop"]:
        await ctx.reply("You can only spam one message at a time.")
		
    else:
        await ctx.send("only for DaHud")
					
					#but i must finish a school project first
#oo ok funi

@client.command(aliases=["spamstop"])
async def stopspam(ctx):
	guild = str(ctx.guild.id)
	await createacc(guild)
	spamtyp[guild]["loop"] = False
	await ctx.send("Stopped the spam.")

@client.command(aliases=["repeat"])
@cooldown(1, 10, BucketType.default)
async def _repeat(ctx, *, user_input):
    time.sleep(float(0.1))
    print("repeat command activated")
    #await ctx.message.delete()
    await ctx.send(f"{user_input}")
    await asyncio.sleep(2)
    print("repeat command finished")
    
@client.command(aliases=["say"])
async def _say(ctx, *, user_input):
    time.sleep(float(0.1))
    print("say command activated")
    #await ctx.message.delete()
    await ctx.channel.purge(limit = 1)
    await ctx.send(f"{user_input}")
    await asyncio.sleep(0.1)
    print("say command finished")


@client.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, user_question):
    author_name = ctx.author.display_name
    responses = [
        "As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes – definitely.",
        "You may rely on it.",
        "No it'll never happen give up.",
        "It might happen but ehhhhhhh.",
        "stfu i aint god."]
    responses2 = ["Yes.", "Without a doubt", "Yes - definitely"]
    final_response = random.choice(responses)
    embed = discord.Embed(
        title = "8ball command",
        description = f"**🎱 Question 🎱: **{user_question}**\n🎱 Answer 🎱: **{final_response}",
        color = random.choice(colours)
    )
    embed.set_footer(icon_url = ctx.author.avatar,text = f"Requested by {author_name}\n" + Version)
    await ctx.send(embed = embed)
    await ctx.message.add_reaction('🔮')
    print ("8ball finished")
#update
@client.command(aliases=["Update", "update", "version", "Version"])
async def _update(ctx):
    author_name = ctx.author.display_name
    responses ="Currently In " + Version + ", the " + Versiondesc + " update."
    final_response = responses
    embed = discord.Embed(
        title = "**Version**",
        description = f"**{final_response}**",
        color = random.choice(colours)
    )
    embed.set_footer(icon_url = ctx.author.avatar,text = f"Requested by {author_name}")
    await ctx.send(embed = embed)
    print ("Version shown")

        


@client.command()
async def dice(ctx):
    dice_number = randint(1,12)
    await ctx.send(dice_number)

@client.command(aliases=["boobs", "Boobs", "BOOBS"])
async def _bobs(ctx):
    await ctx.send("https://tenor.com/view/boob-bobs-big-boob-fruit-orange-gif-15486982")

def sub(x: float, y: float):
    return x - y

def _add(x:float, y:float):
    return x + y

def div(x:float, y:float):
    return x / y

def mult(x:float, y:float):
    return x * y

def _rando(x: int, y: int):
    return random.randint(x, y)

def sqrt(x: float):
    return math.sqrt(x)


@client.command()
async def add(ctx, x: float=None, y: float=None):
    if x == None or y == None:
	    await ctx.reply("Mention the two numbers smh")
    else:
	    res = _add(x, y)
	    await ctx.send(res)

@client.command()
async def subtract(ctx, x: float=None, y:float=None):
    if x == None or y == None:
	    await ctx.reply("Mention the two numbers smh")
    else:
	    res = sub(x, y)
	    await ctx.send(res)

@client.command()
async def divide(ctx, x: float=None, y: float=None):
    if x == None or y == None:
	    await ctx.reply("Mention the two numbers smh")
    else:
	    res = div(x, y)
	    await ctx.send(res)

@client.command()
async def multiply(ctx, x: float=None, y: float=None):
    if x == None or y == None:
	    await ctx.reply("Mention the two numbers smh")
    else:
	    res = mult(x, y)
	    await ctx.send(res)

@client.command()
async def rndm(ctx, x: int=None, y: int=None):
    if x == None or y == None:
	    await ctx.reply("Mention the two numbers smh")
    else:
	    res = _rando(x, y)
	    await ctx.send(res)

@client.command(aliases = ["sqrt"])
async def root(ctx, x: int=None):
    if x == None:
	    await ctx.reply("Mention your number")
    else:
	    res = sqrt(x)
	    await ctx.send(res)

@client.command()
async def square(ctx, x: int=None):
    if x == None:
	    await ctx.reply("Mention your number")
    else:
	    res = x*x
	    await ctx.send(res)
##End of math



@client.command(aliases=["website", "Website"])
async def _website(ctx):
    await ctx.send("http://awesomebot.website2.me/")

'''@client.group(invoke_without_command = True,aliases =
["help", "Help"])
async def _help(ctx,*,args=""):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Help menu commands:**",
        description = "`*adminhelp` for admin commands \n `*8ball` to get a free response \n `*Dice` to get a random number between 1-12 \n `*Owner` to ping Dahud \n `*Pause` to pause a song \n `*Resume` to resume a song\n `*Repeat` to repeat your message \n `*Dict` (word) to get a link to the words definition \n `*Playlist` for the most poggers playlist\n `*Boobs` (not what you think i promise) \n `*Version` for info in the version \n `*Website` for awesomebots personal website\n `*Snipe` To snipe a message \n `*Embed` for a custom embed (use "" for a message longer than 1 word) \n add `dm` to the end of a help menu command to be dm'ed it",
        color = random.choice(colours)
    )
    embed.set_footer(icon_url = ctx.author.avatar,text = f"Requested by {author_name}\n If There Are Any Issues Contact DaHud100#2668 \n" + Version)
    if args.lower() == "dm":
      try:
        await ctx.author.send(embed=embed)
      except:
        await ctx.reply(f"❎ An error occurred!")
    else:
        await ctx.send(embed = embed)
    await ctx.message.add_reaction('🥰')'''

@client.group(invoke_without_command = True,aliases =
["adminhelp", "Adminhelp", "Admin Help", "Admin help", "admin help"])
@commands.has_permissions(manage_messages=True)
async def _adminhelp(ctx,*,args=""):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "Please Use the new `*help` command",
        color = random.choice(colours)
    )
    embed.set_footer(icon_url = ctx.author.avatar,text = f"Requested by {author_name}\n If There Are Any Issues Contact DaHud100#2668 \n" + Version)
    if args.lower() == "dm":
      try:
        await ctx.author.send(embed=embed)
      except:
        await ctx.reply(f"❎ An error occurred!")
    else:
        await ctx.send(embed = embed)
    await ctx.message.add_reaction('🥰')

@client.group(invoke_without_command = True,aliases =
["hacks", "Hacks", "hack", "Hack"])
async def _hackhelp(ctx,*,args=""):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**New Menu:**",
        description = "Please Use the new `*help` command",
        color = random.choice(colours)
    )
    embed.set_footer(icon_url = ctx.author.avatar,text = f"Requested by {author_name}\n If There Are Any Issues Contact DaHud100#2668 \n" + Version)
    if args.lower() == "dm" and ctx.author.id in adminid:
      try:
        await ctx.author.send(embed=embed)
      except:
        await ctx.reply(f"❎ An error occurred!")
    else:
        if ctx.author.id in adminid:
            await ctx.send(embed = embed)
            await ctx.message.add_reaction('🥰')



Memes = ["Meme1.mp4", "Meme2.mp4", "Meme3.mp4", "Meme4.mp4"] 

@client.command(aliases=["meme", "Meme", "video", "Video"])
async def _video(ctx):
	area = ctx.message.channel
	await area.send(file = discord.File(random.choice(Memes)))

@client.command(aliases=["Embed", "embed"])
async def _embed(ctx, content=""):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Custom Embed:**",
        description = f"{content}",
        color = random.choice(colours)
    )
    embed.set_footer(icon_url = ctx.author.avatar, text = f"Requested by {author_name}\n If There Are Any Issues Contact DaHud100#2668 \n" + Version)
    await ctx.send(embed=embed)

@client.command(aliases=["av", "Av", "Avatar", "avatar"])
async def _av(ctx,member:discord.Member=None, args=""):
    if member is None:
      member = ctx.author
    if args.lower() == "dm":
      try:
        await ctx.author.send(member.avatar)
      except:
        await ctx.reply(f"❎ An error occurred!")
    else:
        await ctx.send(member.avatar)
    await ctx.message.add_reaction('🥰')


@client.group(invoke_without_command = True,aliases =
["Hexembed", "hexembed", "Hex Embed", "hex embed", "hex Embed", "Hex embed"])
async def _hex(ctx, hexa, args=""):
    author_name = ctx.author.display_name
    test = hexa
    try:
	    hexa = f"0x{hexa}"
	    hexa = int(hexa,16)
	    hexa = int(hexa)
	    #print(hexa)
	    #hexa = hex(hexa)
	    embed = discord.Embed(
        title = "**Custom Hex Color Embed-**",
        description = f"Used code 0x{test} as embed color integer: {hexa}",
        color = hexa)
	    embed.set_footer(icon_url = ctx.author.avatar, text = f"Requested by {author_name}\n If There Are Any Issues Contact DaHud100#2668 \n" + Version)
	    if args.lower() == "dm":
	      try:
	        await ctx.author.send(embed=embed)
	      except:
	        await ctx.reply(f"❎ An error occurred!")
	    else:
	        await ctx.send(embed = embed)
	    await ctx.message.add_reaction('🥰')
    except Exception as e:
	    await ctx.send(f"Invalid colour code.\n{e}")
			

@client.group(invoke_without_command = True, aliases =
["mathhelp", "Mathhelp"])
async def _mathhelp(ctx,*,args=""):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**New Menu:**",
        description = "Please Use the new `*help` command",
        color = random.choice(colours)
    )
    embed.set_footer(icon_url = ctx.author.avatar, text = f"Requested by {author_name}\n If There Are Any Issues Contact DaHud1001#2668\n" + Version)
    if args.lower() == "dm":
      try:
        await ctx.author.send(embed=embed)
      except:
        await ctx.reply(f"❎ An error occurred!")
    else:
        await ctx.send(embed = embed)
    await ctx.message.add_reaction('🥰')

#Colors 0xCC0000, 0x00ff44, 0x33BAFF
client.sniped_messages = {}
snipe_message_author = None

@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)



@client.command(aliases=["snipe", "Snipe"])
async def snip(ctx, args=""):
    contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]
    embed = discord.Embed(title = "**Deleted Message:**", description=contents, color=random.choice(colours), timestamp=time)
    embed.set_footer(icon_url = ctx.author.avatar, text=f"\n{author.display_name} Deleted in: {channel_name}\n" + Version)
    if args.lower() == "dm":
      try:
        await ctx.author.send(embed=embed)
      except:
        await ctx.reply(f"❎ An error occurred!")
    else:
        await ctx.send(embed = embed)
    await ctx.message.add_reaction('🥰')

@client.command(aliases=["Fortnite", "fortnite", "battlepass", "Battlepass", "Fortnite battlepass", "fortnite battle pass"])
async def _fortnite(ctx):
    await ctx.send("😩 Fortnite battle pass ⚔️ ")
    await asyncio.sleep(0.8)
    await ctx.send("😎 I just shit out my ass 🥶 ")
    await asyncio.sleep(0.8)
    await ctx.send("🥵 Booted up my PC 😤 ")
    await asyncio.sleep(0.8)
    await ctx.send(" 🙏 cuz I need need me 😬 ")
    await asyncio.sleep(0.8)
    await ctx.send(" 😏 get that Fortnite battle pass 😈 ")
    await asyncio.sleep(0.8)
    await ctx.send("🤪 I like Fortnite 🦍 ")
    await asyncio.sleep(0.8)
    await ctx.send("🤔 did I mention Fortnite 🥸")
    await asyncio.sleep(0.8)
    await ctx.send(" 😝 I like Fortnite 😖 ")
    await asyncio.sleep(0.8)
    await ctx.send("🗿 Its night time 😴 ")
    await asyncio.sleep(0.8)
    await ctx.send("🕰️ I mean its 5 o’clock thats basically night time 🤥")
    await asyncio.sleep(0.8)
    await ctx.send("😔 Y’all remember cartoon network adventure time 😶‍🌫️")
##
    

    

#@client.listen("on_message")
#async def _lily(message):
#    if message.author.bot:
#        return
 #   if "<@662093332821835780>" in message.content:
  #      await message.channel.send("if ur not the drug dealer go away")
   # if "<@!662093332821835780>" in message.content:
    #    await message.channel.send("if ur not the drug dealer go away")


#VOICE CHANNEL JOIN
@client.command(pass_context = True, aliases = ["Join", "join", "j", "J", "connect", "Connect"])
async def _join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if ctx.author.id in nouse:
        await ctx.reply ("LMAO ask dahud to remove you form the naughty list")
    elif voice and voice.is_connected():
        await voice.move_to(channel)
        await ctx.send("I joined da vc :D")
        print("Awesome Bot joined a voice channel")
    else:
        await channel.connect()
        await ctx.send(f"I joined `{channel}` :D")
        print("Awesome bot joined a voice channel")
        await ctx.message.add_reaction("👍")



#VOICE CHANNEL LEAVE
@client.command(pass_context = True, aliases = ["Leave", "leave", "L", "l", "Disconnect", "disconnect"])
async def _leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)
    
    if ctx.author.id in nouse:
        await ctx.reply ("LMAO ask dahud to take you off the naughty list")
    elif voice and voice.is_connected():
        await voice.disconnect()
        print(f"Awesome bot disconnected from {channel} voice channel")
        await ctx.send(f"I left `{channel}` :(")    
        await ctx.message.add_reaction('😭')
    else:
        print("command given to leave voice channel but bot wasn't in a voice channel")
        await ctx.send("I wasnt in any channels so I cant disconnect XD")
    
        #awesome bot is a awesome bot with much code coming from a man named kiet pham

#VOICE CHANNEL PLAY YOUTUBE URL
@client.command(pass_context = True, aliases = ["play", "Play", "p", "P"])
async def _play(ctx, url: str):
    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_queue = length - 1 #outprints how many are left in queue after new song is played
            try:
                first_file = os.listdir(DIR)[0] #first file inside directory
            except:
                print("There aint no more songs left in queue yall\n")
                queues.clear
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "//" + first_file)
            
            if length != 0:
                print("Song finished playing, loading next song\n")
                print(f"Number of songs still in queue: {still_queue}")
                is_song_there = os.path.isfile("song.mp3")
                if is_song_there: 
                    os.remove("song.mp3")
                shutil.move(song_path, main_location) #moves queued song to main directory
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                vcvoice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e: check_queue()) #plays the song
                vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
                vcvoice.source.value = 0.05
            
            else: #if queues = 0, clearns it
                queues.clear()
                return

        else: #is there is no queue folder
            queues.clear()
            print("There are no songs queued after the last song\n")

    #end of queue section thingy for play command
    is_song_there = os.path.isfile("song.mp3")
    try: #code will try to remove song, if it's playing then no remove
        if is_song_there:
            os.remove("song.mp3")
            queues.clear()
            print("I removed an old crusty song file")
    except PermissionError:
        print("I failed to remove song file, it was in use sorry :(")
        ctx.send("Error: I cant play the same file at the same time")
        return

    
    #this section is here to remove the old queue folder
    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:   #if there is an old queue file, it will try to remove it
            print("I removed the old queue folder")
            shutil.rmtree(Queue_folder)
    except:
        print("aint no old queue folder")

    #rest of play command to play songs
    await ctx.send("Am gettin da pro musica ready for ur ears")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "512",
        }], #code above to specify options in ydl
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloaded audio file\n")
        ydl.download([url])
    #renames file name 
    for file in os.listdir("./"): #./ for current directory
        if file.endswith(".mp3"):
            audio_file_name = file
            print(f"Renamed File {file}\n")
            os.rename(file, "song.mp3")
    #checks to see if audio has finished playing, after then it will print
    vcvoice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e: check_queue())
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05
    new_name = audio_file_name.rsplit("-", 2)
    await ctx.send(f"Am plaing {new_name}")
    print("playing\n")


#VOICE CHANNEL MUSIC PAUSE COMMAND
@client.command(pass_context = True, aliases = ["pause", "Pause"])
async def _pause(ctx):
    voice = get(client.voice_clients, guild = ctx.guild)
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    
    if vcvoice and voice.is_playing():
        vcvoice.pause()
        print("Music paused")
        await ctx.send("I paused da music")
    else:
        print("Music wasn't playing but there was a request to pause music")
        await ctx.send("There was no music to pause dummy :P")


#VOICE CHANNEL MUSIC RESUME COMMAND
@client.command(pass_context = True, aliases = ["resume", "Resume" , "r" , "R"])
async def _resume(ctx):
    voice = get(client.voice_clients, guild = ctx.guild)
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    
    if vcvoice and voice.is_paused():
        vcvoice.resume()
        print("Music resumed")
        await ctx.send("Resumed your music :D")
        await ctx.message.add_reaction('🎶')
    else:
        print("Music was not paused but a request was sent for music pause")
        await ctx.send("The music was playing u cant resume it stoopid")
        await ctx.message.add_reaction('😆')

#VOICE CHANNEL MUSIC STOP COMMAND
@client.command(pass_context = True, aliases = ["stop", "Stop"])
async def _stop(ctx):
    voice = get(client.voice_clients, guild = ctx.guild)
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    queues.clear() #clears queue when stop command ran

    if vcvoice and voice.is_playing():
        vcvoice.stop()
        print("Music stopped")
        await ctx.send("Music stopped")
    else:
        print("Music could not be stopped")
        await ctx.send("Music can't be stopped if there isn't music playing")

#HELP - SOUNDBOARD COMMANDS
@client.command(aliases = ["sbhelp", "Sbhelp", "SBhelp", "soundboardhelp", "Soundboard Help", "soundboard Help", "sb help", "SB help", "Sb help", "soundboard help", "Soundboard help", "SB Help", "sb Help"])
async def _help_soundboard(ctx,*,args=""):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**New Menu**",
        description = "Please Use the new `*help` command",
        color = random.choice(colours)
    )
    embed.set_footer(icon_url = ctx.author.avatar,text = f"Requested by {author_name}\n" + Version)
    if args.lower() == "dm":
      try:
        await ctx.author.send(embed=embed)
      except:
        await ctx.reply(f"❎ An error occurred!")
    else:
        await ctx.send(embed = embed)
    await ctx.message.add_reaction('🥰')

@client.group(invoke_without_command = True, aliases = ["sb", "SB", "soundboard", "Soundboard", "SoundBoard"])
async def _soundboard(ctx):
    await ctx.send("please format command differently")

#SB AIRHORN 
@_soundboard.command(aliases = ["airhorn", "Airhorn"])
async def _soundboard_airhorn(ctx):
    await ctx.send("Playing **airhorn** sound effect from soundboard")
    print("\nPlayed airhorn sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/airhorn.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB ALI-A SOUNDTRACK
@_soundboard.command(aliases = ["ali_a", "alia", "Ali-a", "Alia"])
async def _soundboard_ali_a(ctx):
    await ctx.send("Playing **ali_a** sound effect from soundboard")
    print("\nPlayed ali_a sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/ali_a.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB BEGONE THOT
@_soundboard.command(aliases = ["begone_thot", "begonethot", "Begone_thot", "Begonethot"])
async def _soundboard_begone_thot(ctx):
    await ctx.send("Playing **begone_thot** sound effect from soundboard")
    print("\nPlayed begone_thot sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/begone_thot.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DAMN SON WHERE'D U FIND THIS
@_soundboard.command(aliases = ["damn_son", "Damn_son", "damnson", "Damnson"])
async def _soundboard_damn_son(ctx):
    await ctx.send("Playing **damn_son** sound effect from soundboard")
    print("\nPlayed damn_son sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/damn_son.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DANKSTORM
@_soundboard.command(aliases = ["dankstorm", "Dankstorm"])
async def _soundboard_dankstorm(ctx):
    await ctx.send("Playing **dankstorm** sound effect from soundboard")
    print("\nPlayed dankstorm sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/dankstorm.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DEEZNUTS
@_soundboard.command(aliases = ["deez_nuts", "deeznuts", "Deez_nuts", "Deeznuts"])
async def _soundboard_deez_nuts(ctx):
    await ctx.send("Playing **deez_nuts** sound effect from soundboard")
    print("\nPlayed deez_nuts sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/deez_nuts.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DEJA VU
@_soundboard.command(aliases = ["deja_vu", "dejavu", "Deja_vu", "Dejavu"])
async def _soundboard_deja_vu(ctx):
    await ctx.send("Playing **deja_vu** sound effect from soundboard")
    print("\nPlayed deja_vu sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/deja_vu.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

@_soundboard.command(aliases = ["dis_dude", "this_dude", "disdude", "thisdude", "Dis_dude", "This_dude", "Disdude", "Thisdude" ])
async def _soundboard_this_dude(ctx):
    await ctx.send("Playing **dis_dude** sound effect from soundboard")
    print("\nPlayed dis_dude sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/dis_dude.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB ANOTHER FAG LEFT THE CHAT
@_soundboard.command(aliases = ["f_left", "fleft", "F_left", "Fleft"])
async def _soundboard_f_left(ctx):
    await ctx.send("Playing **f_left** sound effect from soundboard")
    print("\nPlayed f_left sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/f_left.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB FART
@_soundboard.command(aliases = ["fart", "Fart"])
async def _soundboard_fart(ctx):
    await ctx.send("Playing **fart** sound effect from soundboard")
    print("\nPlayed fart sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/fart.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB HAH GAAAYY
@_soundboard.command(aliases = ["ha_gay", "hagay", "Ha_gay", "Hagay"])
async def _soundboard_hah_gay(ctx):
    await ctx.send("Playing **hah_gay** sound effect from soundboard")
    print("\nPlayed hah_gay sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/hah_gay.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB IT'S CALLED HENTAI, AND IT'S ART
@_soundboard.command(aliases = ["hen_art", "henart", "Hen_art", "Henart"])
async def _soundboard_hentai_art(ctx):
    await ctx.send("Playing **henart (hentai art)** sound effect from soundboard")
    print("\nPlayed henart sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/hen_art.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB ILLUMINATI X-FILES SOUNDTRACK
@_soundboard.command(aliases = ["illuminati", "Illuminati"])
async def _soundboard_illuminati(ctx):
    await ctx.send("Playing **illuminati** sound effect from soundboard")
    print("\nPlayed illuminati sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/illuminati.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB BITCH LASAGNA
@_soundboard.command(aliases = ["lasagna", "Lasagna", "bitch_lasagna", "Bitch_lasagna"])
async def _soundboard_bitch_lasagna(ctx):
    await ctx.send("Playing **bitch_lasagna** sound effect from soundboard")
    print("\nPlayed bitch_lasagna sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/lasagna.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB LOOSER
@_soundboard.command(aliases = ["looser", "Looser", "loser", "Loser"])
async def _soundboard_loser(ctx):
    await ctx.send("Playing **loser** sound effect from soundboard")
    print("\nPlayed loser sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/loser.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB NOOB 
@_soundboard.command(aliases = ["noob", "Noob"])
async def _soundboard_noob(ctx):
    await ctx.send("Playing **noob** sound effect from soundboard")
    print("\nPlayed noob sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/noob.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB OOF SOUND
@_soundboard.command(aliases = ["oof", "Oof"])
async def _soundboard_oof(ctx):
    await ctx.send("Playing **oof** sound effect from soundboard")
    print("\nPlayed oof sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/oof.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB I'M PICKLE RICKKKK
@_soundboard.command(aliases = ["pickle_rick", "Pickle_rick", "picklerick", "Picklerick"])
async def _soundboard_pickcle_rick(ctx):
    await ctx.send("Playing **pickle_rick** sound effect from soundboard")
    print("\nPlayed pickle_rick sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/pickle_rick.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB *POP* NICE  
@_soundboard.command(aliases = ["nice", "Nice"])
async def _soundboard_nice(ctx):
    await ctx.send("Playing **nice** sound effect from soundboard")
    print("\nPlayed nice sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/nice.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB WHY DON'T WE JUST RELAX, TURN ON THE RADIO, WOULD YOU LIKE AM OR FM
@_soundboard.command(aliases = ["radio", "Radio"])
async def _soundboard_radio(ctx):
    await ctx.send("Playing **radio** sound effect from soundboard")
    print("\nPlayed radio sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/radio.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB RICKROLL
@_soundboard.command(aliases = ["rick_roll", "Rick_roll", "rickroll", "Rickroll"])
async def _soundboard_rick_roll(ctx):
    await ctx.send("Playing **rick_roll** sound effect from soundboard")
    print("\nPlayed rick_roll sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/rick_roll.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB SPARTA
@_soundboard.command(aliases = ["sparta", "Sparta"])
async def _soundboard_sparta(ctx):
    await ctx.send("Playing **sparta** sound effect from soundboard")
    print("\nPlayed sparta sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/sparta.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB TITANIC FLUTE MEME
@_soundboard.command(aliases = ["titanic", "Titanic"])
async def _soundboard_titanic(ctx):
    await ctx.send("Playing **titanic** sound effect from soundboard")
    print("\nPlayed titanic sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/titanic.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB GTAV WASTED SOUND
@_soundboard.command(aliases = ["wasted", "Wasted"])
async def _soundboard_wasted(ctx):
    await ctx.send("Playing **wasted** sound effect from soundboard")
    print("\nPlayed wasted sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/wasted.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

@_soundboard.command(aliases = ["wideputin", "Wideputin", "wide putin", "Wide Putin", "wide Putin"])
async def _soundboard_wide_putin(ctx):
    await ctx.send("Playing **wide_putin** sound effect from soundboard")
    print("\nPlayed wide_putin sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/wideputin.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05
#SB RICK & MORTY WUBBA LUBBA DUB DUB
@_soundboard.command(aliases = ["wubba", "Wubba"])
async def _soundboard_wubba(ctx):
    await ctx.send("Playing **wubba** sound effect from soundboard")
    print("\nPlayed wubba sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/wubba.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05


@_soundboard.command(aliases = ["yes", "Yes"])
async def _soundboard_yes(ctx):
    await ctx.send("Playing **yes** sound effect from soundboard")
    print("\nPlayed yes sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/Talking Ben Yes Sound Effect.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

@_soundboard.command(aliases = ["no", "No"])
async def _soundboard_no(ctx):
    await ctx.send("Playing **no** sound effect from soundboard")
    print("\nPlayed no sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/Talking Ben No Sound Effect.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

@_soundboard.command(aliases = ["oh great heavens", "ohgreatheavens", "Oh Great Heaves"])
async def _soundboard_ohheavens(ctx):
    await ctx.send("Playing **Oh Great Heavens** sound effect from soundboard")
    print("\nPlayed OhGreatHeavens sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/Ohh great heavens Sound Effect.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05
#VOICE CHANNEL MUSIC QUEUE
#this command is for music to be queued up if you use the "cv6 play" multiple times while music is still playing
queues = {}

#ERROR HANDLING
@_chat_clear.error
async def _chat_clear(ctx, error):
	if isinstance(error, commands.errors.CommandInvokeError):
		await ctx.reply("I don't have `Manage Messages` permission. Enable it to use this command.")

@snip.error
async def _chat_clear(ctx, error):
	if isinstance(error, commands.errors.CommandInvokeError):
		await ctx.reply("Nothing to snipe lmao")

@_embed.error
async def _chat_clear(ctx, error):
	if isinstance(error, commands.errors.CommandInvokeError):
		await ctx.reply("Put something to embed lmao")
#admin id?
        
'''async def openaccount(user):
	users = await getdata()

	if str(user.id) in users:
		return False
	else:
		users[str(user.id)] = {}
        users[str(user.id)][""]
		

		with open("accounts.json", "w") as f:
			json.dump(users, f)
		return True

async def getdata():
	with open("accounts.json", "r") as f:
		users = json.load(f)
	return users


@client.command(aliases = ["balance"])
async def bal(ctx,*,member: discord.Member = None):
	if member == None:
		member = ctx.author
	await openaccount(member)
	users = await getdata()''' 

@my_personal_purge.error
async def _chat_clear(ctx, error):
	if isinstance(error, commands.errors.CommandInvokeError):
		await ctx.reply("Put something to embed lmao")



''''@client.command(pass_context = True, aliases = ["Queue", "queue", "Q", "q"])
async def _queue(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")      #sees if there is any song files in queue, if there is any then it counts them
    DIR = os.path.abspath(os.path.realpath("Queue"))
    queue_num = len(os.listdir(DIR)) #gets/counts ammount of files in the queue
    queue_num += 1 #adds another to queue
    add_queue = True
    while add_queue:
        if queue_num in queues:
            queue_num += 1
        else:
            add_queue = False
            queues[queue_num] = queue_num

    queue_path = os.path.abspath(os.path.realpath("Queue") + f"//song{queue_num}.%(ext)s")
    #takes the real path of song in queue and number of it
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl" : queue_path,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "512",
        }], #code above to specify options in ydl
    }
    #downloads song and puts into queue path above ^
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloaded audio file\n")
        ydl.download([url])
    await ctx.send("Adding song " + str(queue_num) + " to the queue")
    print("added a song to queue\n")

    class Music(commands.Cog):
        "Music related commands.

    __slots__ = ('bot', 'players')

    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    async def cleanup(self, guild):
        try:
            await guild.voice_client.disconnect()
        except AttributeError:
            pass

        try:
            del self.players[guild.id]
        except KeyError:
            pass

    async def __local_check(self, ctx):
        """A local check which applies to all commands in this cog."""
        if not ctx.guild:
            raise commands.NoPrivateMessage
        return True

    async def __error(self, ctx, error):
        """A local error handler for all errors arising from commands in this cog."""
        if isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.send('This command can not be used in Private Messages.')
            except discord.HTTPException:
                pass
        elif isinstance(error, InvalidVoiceChannel):
            await ctx.send('Error connecting to Voice Channel. '
                           'Please make sure you are in a valid channel or provide me with one')

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    def get_player(self, ctx):
        """Retrieve the guild player, or generate one."""
        try:
            player = self.players[ctx.guild.id]
        except KeyError:
            player = MusicPlayer(ctx)
            self.players[ctx.guild.id] = player

        return player

    @commands.command(name='join', aliases=['connect', 'j'], description="connects to voice")
    async def connect_(self, ctx, *, channel: discord.VoiceChannel=None):
        """Connect to voice.
        Parameters
        ------------
        channel: discord.VoiceChannel [Optional]
            The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
            will be made.
        This command also handles moving the bot to different channels.
        """
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                embed = discord.Embed(title="", description="No channel to join. Please call `,join` from a voice channel.", color=discord.Color.green())
                await ctx.send(embed=embed)
                raise InvalidVoiceChannel('No channel to join. Please either specify a valid channel or join one.')

        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Moving to channel: <{channel}> timed out.')
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Connecting to channel: <{channel}> timed out.')
        if (random.randint(0, 1) == 0):
            await ctx.message.add_reaction('👍')
        await ctx.send(f'**I joined `{channel}`**')

    @commands.command(name='play', aliases=['sing','p'], description="streams music")
    async def play_(self, ctx, *, search: str):
        """Request a song and add it to the queue.
        This command attempts to join a valid voice channel if the bot is not already in one.
        Uses YTDL to automatically search and retrieve a song.
        Parameters
        ------------
        search: str [Required]
            The song to search and retrieve using YTDL. This could be a simple search, an ID or URL.
        """
        await ctx.trigger_typing()

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = self.get_player(ctx)

        # If download is False, source will be a dict which will be used later to regather the stream.
        # If download is True, source will be a discord.FFmpegPCMAudio with a VolumeTransformer.
        source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=False)

        await player.queue.put(source)

    @commands.command(name='pause', description="pauses music")
    async def pause_(self, ctx):
        """Pause the currently playing song."""
        vc = ctx.voice_client

        if not vc or not vc.is_playing():
            embed = discord.Embed(title="", description="I am currently not playing anything", color=discord.Color.green())
            return await ctx.send(embed=embed)
        elif vc.is_paused():
            return

        vc.pause()
        await ctx.send("Paused ⏸️")

    @commands.command(name='resume', description="resumes music")
    async def resume_(self, ctx):
        """Resume the currently paused song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)
        elif not vc.is_paused():
            return

        vc.resume()
        await ctx.send("Resuming ⏯️")

    @commands.command(name='skip', description="skips to next song in queue")
    async def skip_(self, ctx):
        """Skip the song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)

        if vc.is_paused():
            pass
        elif not vc.is_playing():
            return

        vc.stop()
    
    @commands.command(name='remove', aliases=['rm', 'rem'], description="removes specified song from queue")
    async def remove_(self, ctx, pos : int=None):
        """Removes specified song from queue"""

        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if pos == None:
            player.queue._queue.pop()
        else:
            try:
                s = player.queue._queue[pos-1]
                del player.queue._queue[pos-1]
                embed = discord.Embed(title="", description=f"Removed [{s['title']}]({s['webpage_url']}) [{s['requester'].mention}]", color=discord.Color.green())
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(title="", description=f'Could not find a track for "{pos}"', color=discord.Color.green())
                await ctx.send(embed=embed)
    
    @commands.command(name='clear', aliases=['clr', 'cl', 'cr'], description="clears entire queue")
    async def clear_(self, ctx):
        """Deletes entire queue of upcoming songs."""

        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        player.queue._queue.clear()
        await ctx.send('**Cleared**')

    @commands.command(name='queue', aliases=['q', 'playlist', 'que'], description="shows the queue")
    async def queue_info(self, ctx):
        """Retrieve a basic queue of upcoming songs."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if player.queue.empty():
            embed = discord.Embed(title="", description="queue is empty", color=discord.Color.green())
            return await ctx.send(embed=embed)

        seconds = vc.source.duration % (24 * 3600) 
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if hour > 0:
            duration = "%dh %02dm %02ds" % (hour, minutes, seconds)
        else:
            duration = "%02dm %02ds" % (minutes, seconds)

        # Grabs the songs in the queue...
        upcoming = list(itertools.islice(player.queue._queue, 0, int(len(player.queue._queue))))
        fmt = '\n'.join(f"`{(upcoming.index(_)) + 1}.` [{_['title']}]({_['webpage_url']}) | ` {duration} Requested by: {_['requester']}`\n" for _ in upcoming)
        fmt = f"\n__Now Playing__:\n[{vc.source.title}]({vc.source.web_url}) | ` {duration} Requested by: {vc.source.requester}`\n\n__Up Next:__\n" + fmt + f"\n**{len(upcoming)} songs in queue**"
        embed = discord.Embed(title=f'Queue for {ctx.guild.name}', description=fmt, color=discord.Color.green())
        embed.set_footer(text=f"{ctx.author.display_name}", icon_url=ctx.author.avatar)

        await ctx.send(embed=embed)

    @commands.command(name='np', aliases=['song', 'current', 'currentsong', 'playing'], description="shows the current playing song")
    async def now_playing_(self, ctx):
        """Display information about the currently playing song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if not player.current:
            embed = discord.Embed(title="", description="I am currently not playing anything", color=discord.Color.green())
            return await ctx.send(embed=embed)
        
        seconds = vc.source.duration % (24 * 3600) 
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if hour > 0:
            duration = "%dh %02dm %02ds" % (hour, minutes, seconds)
        else:
            duration = "%02dm %02ds" % (minutes, seconds)

        embed = discord.Embed(title="", description=f"[{vc.source.title}]({vc.source.web_url}) [{vc.source.requester.mention}] | `{duration}`", color=discord.Color.green())
        embed.set_author(icon_url=self.bot.user.avatar_url, name=f"Now Playing 🎶")
        await ctx.send(embed=embed)

    @commands.command(name='volume', aliases=['vol', 'v'], description="changes Kermit's volume")
    async def change_volume(self, ctx, *, vol: float=None):
        """Change the player volume.
        Parameters
        ------------
        volume: float or int [Required]
            The volume to set the player to in percentage. This must be between 1 and 100.
        """
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I am not currently connected to voice", color=discord.Color.green())
            return await ctx.send(embed=embed)
        
        if not vol:
            embed = discord.Embed(title="", description=f"🔊 **{(vc.source.volume)*100}%**", color=discord.Color.green())
            return await ctx.send(embed=embed)

        if not 0 < vol < 101:
            embed = discord.Embed(title="", description="Please enter a value between 1 and 100", color=discord.Color.green())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)

        if vc.source:
            vc.source.volume = vol / 100

        player.volume = vol / 100
        embed = discord.Embed(title="", description=f'**`{ctx.author}`** set the volume to **{vol}%**', color=discord.Color.green())
        await ctx.send(embed=embed)

    @commands.command(name='leave', aliases=["stop", "dc", "disconnect", "bye"], description="stops music and disconnects from voice")
    async def leave_(self, ctx):
        """Stop the currently playing song and destroy the player.
        !Warning!
            This will destroy the player assigned to your guild, also deleting any queued songs and settings.
        """
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel", color=discord.Color.green())
            return await ctx.send(embed=embed)

        if (random.randint(0, 1) == 0):
            await ctx.message.add_reaction('👋')
        await ctx.send('**Successfully disconnected**')

        await self.cleanup(ctx.guild)


def setup(bot):
    bot.add_cog(Music(bot))'''
#keeps bot online as a webserver

keep_alive()
#client token to run bot
',reconnect=True,bot=True)'
'client.run(token)'
client.run(token)