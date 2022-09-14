import discord
from discord.ext import commands

import io

from backend import Timetable
from db_handler import add, get

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="?", intents=intents)


@client.event
async def on_ready():
    print("ready")
    
@client.command()
async def set_timetable(ctx: commands.Context, *args) -> None:
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
async def timetable(ctx: commands.Context) -> str:
    ttbl = get(str(ctx.message.author), "timetable")
    ttbl = Timetable().expand(ttbl)
    
    image = Timetable().table_img(ttbl)
    with io.BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))


    
client.run("Token :D")
