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
        ttbl_handler.get_timetable()
        
    else:
        await ctx.send("Looks like you haven't attached an image")
        
@client.command()
async def timetable(ctx: commands.Context, user="default") -> None:
    usr = str(ctx.message.author) if user == "default" else str(ctx.message.mentions[0]._user)
    
    if db_handler.find(usr, "timetable"):
        ttbl = db_handler.get(usr, "timetable")
        ttbl = ttbl_handler.expand(ttbl)
        
        image = ttbl_handler.table_img(ttbl)
        if db_handler.find(usr, "color"):
            image = ttbl_handler.add_mask(image, tuple(db_handler.get(usr, "color")))
        
        with io.BytesIO() as image_binary:
            image.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))
    
    else:
        await ctx.send("Oops, looks like {} set up a timetable yet.".format("you haven't" if user == "default" else (usr[:-5] + " hasn't")))

@client.command()
async def timetable_color(ctx: commands.Context, r: str, g: str, b: str) -> None:
    db_handler.add(str(ctx.message.author), ["color", (int(r), int(g), int(b))])
    await ctx.send("Saved!")
    
client.remove_command('help')
@client.command()
async def help(ctx: commands.Context) -> None:
    embed = discord.Embed(title=f"__**Help**__", color=0x03f8fc)
    embed.add_field(name='__?timetable [user (optional)]__', value='**Shows Timetable**\n ↳ user ⇢ _the user whose timetable you want to see. Leave blank if you want to see your own_', inline=False)
    embed.add_field(name='__?set_timetable [timetable]__', value='**Sets the timetable**\n ↳ timetable ⇢ _text input with subjects separated by "," and days separated by "|"_', inline=False)
    embed.add_field(name='__?timetable_color [r] [g] [b]__', value='**Sets the colour of the timetable**\n ↳ r ⇢ _sets red value of desired colour_\n ↳ g ⇢ _sets green value of desired colour_\n ↳ b ⇢ _sets blue value of desired colour_', inline=False)
    embed.add_field(name='__?help__', value='**Displays this message**', inline=False)
    
    await ctx.send(embed=embed)

client.run("Token :P")