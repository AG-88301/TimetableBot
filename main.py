import discord
from discord.ext import commands

from backend import Timetable
from db_handler import add

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="?", intents=intents)


@client.event
async def on_ready():
    print("ready")
    
@client.command()
async def set_timetable(ctx, *args):
    if len(args) != 0:
        ttbl = Timetable()
        add(str(ctx.message.author), ["timetable", str(ttbl.compress(ttbl.expand(args)))])
        await ctx.send("Saved!")
        
    elif len(ctx.message.attachments) != 0:
        img = ctx.message.attachments[0]
        await img.save("img.jpg")
        Timetable("img.jpg").get_timetable()
        
    else:
        await ctx.send("Looks like you haven't attached an image")
        
@client.command()
async def timetable(ctx):
    pass
    
client.run("MTAxODE3NzI3MDMwMjY0MjIwNg.GZ1H-q.mCEKiew8qc-SEUSEHhGYdYi5Ta5F5Lbizv6Stg")