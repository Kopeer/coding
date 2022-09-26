import datetime
import discord

popcat = 0
client = discord.Client()

@client.event
async def on_ready() :
    print("bot get starting...")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("I'm Online!"))

@client.event
async def on_message(message) :
    if message.content == ".imjiho" :
        await message.channel.send("{} | {} You are jiho? wow you are ####".format(message.author, message.author.mention))

    elif message.content == ".hello" :
        await message.channel.send("{} | {} Hello There! Welcome to 동준 서버!".format(message.author, message.author.mention))
    
    elif message.content == ".Popcat" :
        global popcat
        popcat = popcat + 1
        embed = discord.Embed(title = "PopCat", description="pop and pops")
        embed.add_field(name="Clicks", value=popcat)
        embed.set_thumbnail(url="https://c.tenor.com/_1hMqyFC4LEAAAAC/pop-cat.gif")

        await message.channel.send (embed = embed)

    
    elif message.content == ".1+1" :
        await message.channel.send("{} | {} 1 + 1 is 2.".format(message.author, message.author.mention))

    elif message.content == ".time" :
        await message.channel.send("{} | {} The time now is " + datetime.Now + " .".formet(message.author, message.author.mention))

    elif message.content == ".ver" :
        await message.channel.send("{} | {} Verstion 1.0.5 \n made by 떵즈이".format(message.author, message.author.mention))

    elif message.content == ".jiho" :
        await message.channel.send("babo")

    elif message.content == ".dongjun" :
        await message.channel.send("{} | {} mongchongyee".format(message.author, message.author.mention))

    elif message.content == ".call jiho" :
        await message.channel.send("지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야지호야")

    elif message.content == ".call dongjun" :
        await message.channel.send("떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이떵즈이")

    elif message.content == "ㅋㅋㅋ" :
        await message.channel.send("{} | {} Haha! That's funny!".format(message.author, message.author.mention))

    elif message.content == "'.'" :
        await message.channel.send("{} | {} －O－".format(message.author, message.author.mention))

    elif message.content == ".:)" :
        await message.channel.send("{} | {} :)".format(message.author, message.author.mention))


client.run('MTAwNTc5MjkzMzkzMDM1MjY1MA.GCgmU8.lO7euYIFMpny0J06W5PtKhIzneVC8mo5BxvhfI')