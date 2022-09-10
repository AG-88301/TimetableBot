import discord
from discord.ext import commands

from get_timetable import Timetable

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="?", intents=intents)


@client.event
async def on_ready():
    print("ready")
    
@client.command()
async def set_timetable(ctx):
    if len(ctx.message.attachments) != 0:
        img = ctx.message.attachments[0]
        await img.save("img.jpg")
        Timetable("img.jpg").get_timetable()
    else:
        await ctx.send("Looks like you haven't attached an image")
    
client.run("Private Token :D")
