import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time
import lxml

bot = commands.Bot(command_prefix="*")
client = discord.Client()

entireText = 0
user = []
musictitle = []
song_queue = []
musicnow = []
number = 1

@bot.event
async def on_ready() :
    print("Music_bot is ready!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Music Study"))


@bot.command()
async def h(ctx) :
    await ctx.send("I'm here to help you!\ncommands : \n  *play (music name) : is not done yet.\n  *play_url (music youtube url) : play music by youtube link.(connect is auto.) \n  *pause : pause song. \n  *start : start music. \n  *discon : disconnect voice sever.")


@bot.command()
async def discon(ctx) :
    try :
        await vc.disconnect()
        await ctx.send("Disconnect was succesful.")
    except :
        await ctx.send("Music_bot is already disconnect voice sever.")

@bot.command()
async def play_url(ctx, *, url):

    try :
        global vc
        vc = await ctx.message.author.voice.channel.connect()
        await ctx.send("connect was succesful.")

    except :
        try :
            await vc.move_to(ctx.message.author.voice.channel)

        except :
            await ctx.send("There is no user in voice channel.")

            
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "Music playing : ", description = "now " + url + "is playing..", color = 0x00ff00))
    else:
        await ctx.send("Music is already playing!")


@bot.command()
async def play(ctx, *, msg):
    if not vc.is_playing():
        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = r"C:\Users\tubed\Documents\coding things\discord_bot\chromedriver"
        driver = webdriver.Chrome(chromedriver_dir)
        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "Music Playing : ", description = "Now " + entireText + " is playing..", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("Music is already playing!")

@bot.command()
async def pause(ctx):
    global entireText
    if vc.is_playing():
        vc.pause()
        await ctx.send(embed = discord.Embed(title= "Pause", description = entireText + " is pause now..", color = 0x00ff00))
    else:
        await ctx.send("Not playing music now.")

@bot.command()
async def start(ctx):
    global entireText
    try:
        vc.resume()
    except:
         await ctx.send("Not playing music now.")
    else:
         await ctx.send(embed = discord.Embed(title= "Restart", description = entireText  + " is now playing..", color = 0x00ff00))

@bot.command()
async def off_mus(ctx):
    global entireText
    global number
    number = 0
    if vc.is_playing():
        vc.stop()
        await ctx.send(embed = discord.Embed(title= "Off Music", description = entireText  + " is not playing now..", color = 0x00ff00))
    else:
        await ctx.send("Not playing music now.")

@bot.command()
async def nowpl(ctx):
    global entireText
    if not vc.is_playing():
        await ctx.send("Not playing music now.")
    else:
        await ctx.send(embed = discord.Embed(title = "Now music", description = entireText + " is playing now..", color = 0x00ff00))


bot.run("MTAwNjIwMjMyMzg2MjgyMjk1Mg.GXXmNE.uBCWr3ghsY1X4fLCbF3g7HOtL8t_8bVCRtaP8w")