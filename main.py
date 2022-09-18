import discord
from discord.ext import commands

import io

from backend import Timetable
from db_handler import Database


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="?", intents=intents)

db_handler = Database()
ttbl_handler = Timetable()

@client.event
async def on_ready() -> str:
    print("Ready")
    
@client.command()
async def set_timetable(ctx: commands.Context, *args) -> None:
    if len(args) != 0:
        db_handler.add(str(ctx.message.author), ["timetable", str(ttbl_handler.compress(ttbl_handler.expand(args)))])
        await ctx.send("Saved!")
        
    elif len(ctx.message.attachments) != 0:
        img = ctx.message.attachments[0]
        await img.save("img.jpg")
        Timetable("img.jpg").get_timetable()
        
    else:
        await ctx.send("Looks like you haven't attached an image")
        
@client.command()
async def timetable(ctx: commands.Context, user="default") -> None:
    x = int(str(user)[2:-1])
    print(x)
    author = str(ctx.message.author) if user == "default" else str(ctx.message.author)
    print(author)
    
    ttbl = db_handler.get(author, "timetable")
    ttbl = ttbl_handler.expand(ttbl)
    
    image = ttbl_handler.table_img(ttbl)
    if db_handler.find(author, "color"):
        image = ttbl_handler.add_mask(image, tuple(db_handler.get(author, "color")))
    
    with io.BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))

@client.command()
async def timetable_color(ctx: commands.Context, r: str, g: str, b: str) -> None:
    db_handler.add(str(ctx.message.author), ["color", (int(r), int(g), int(b))])
    await ctx.send("Saved!")
    
@client.command()
async def next(ctx:commands.Context):
    pass
    
client.remove_command('help')
@client.command()
async def help(ctx: commands.Context) -> None:
    embed = discord.Embed(title=f"__**Help**__", color=0x03f8fc)
    embed.add_field(name='?timetable', value='Shows Timetable', inline=False)
    embed.add_field(name='?set_timetable [timetable]', value='Sets the timetable\n + timetable -> text input with subjects separated by "," and days separated by "|"', inline=False)
    embed.add_field(name='?timetable_color [r] [g] [b]', value='Sets the colour of the timetable\n + r -> sets red value of desired colour\n + g -> sets green value of desired colour\n + b -> sets blue value of desired colour', inline=False)
    embed.add_field(name='?help', value='Displays this message', inline=False)
    
    await ctx.send(embed=embed)

client.run("TOKEN >:(")