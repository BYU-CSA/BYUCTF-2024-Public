import disnake
from disnake.ext import commands
import sqlite3
import os

connection = sqlite3.connect("porgs.db")
cursor = connection.cursor()

bot = commands.Bot(command_prefix=commands.when_mentioned)
intents = disnake.Intents.default()


class Porg:
    def __init__(self, data):
        (self.id, self.name, self.age, self.fav_color, self.image) = data


@bot.event
async def on_ready():
    print('Bot is up!')
    if 'TOKEN' in os.environ:
        del os.environ['TOKEN']


@bot.command()
async def helpme(ctx):
    if not isinstance(ctx.channel, disnake.DMChannel):
        await ctx.send("Please DM me to use this command.")
        return

    await ctx.send("""
        helpme - This command
        porg <name> - Find your porg friend
        source - Get my source code
    """)


@bot.command()
async def source(ctx):
    if not isinstance(ctx.channel, disnake.DMChannel):
        await ctx.send("Please DM me to use this command.")
        return
    
    src = disnake.File('code.zip')
    await ctx.send("Here's my source code!", file=src)


@bot.command()
async def porg(ctx, *, name: str):
    if not isinstance(ctx.channel, disnake.DMChannel):
        await ctx.send("Please DM me to use this command.")
        return

    query = f"SELECT * FROM porgs WHERE name LIKE '{name}'"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except Exception as e:
        ctx.send("Error:", str(e))
        return

    if len(results) == 0:
        await ctx.send(f"No Porg found with name {name}")
        return

    result = results[0]
    porg = Porg(result)

    if ('..' in porg.image):
        await ctx.send("Nope!")
        return
    
    img = disnake.File(os.path.join('/srv/images/', porg.image))
    display = disnake.Embed(title=porg.name, color=0x2545d1)
    display.add_field(name="Name", value=porg.name, inline=True)
    display.add_field(name="Age", value=porg.age, inline=True)
    display.add_field(name="Favorite Color", value=porg.fav_color, inline=True)
    display.set_image(file=img)

    await ctx.send(embed=display)


bot.run(os.environ['TOKEN'])
