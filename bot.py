import discord
import requests
import time
import json
import urllib.request 
from discord.ext import commands

site = "https://apps.runescape.com/runemetrics/profile/profile?user="
token = "" #DISCORD TOKEN HERE

client = commands.Bot(command_prefix = '?', help_command=None)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="?help"))
    print('Bot is ready.')


@client.command()
async def check(ctx, *, username):
    z = username.replace(" ", "_")
    with urllib.request.urlopen(f"{site}{z}") as url:
        data = json.loads(url.read().decode())
        a = (list(data.keys())[0])
    if a == "error":
        b = data["error"]
        if b == "NOT_A_MEMBER":
            await ctx.send(f"**{username}** is currently **banned**.")
        if b == "NO_PROFILE":
            await ctx.send(f"**{username}** could be deleted. The username is not associated with a RS3 profile, but is **not** banned. Check ?help for more info.")
        if b == "PROFILE_PRIVATE":
            await  ctx.send(f"**{username}** is fine, not banned.")
    else:
        await ctx.send(f"**{username}** is fine, not banned.")


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title='Help:',
        description="""
        **?check (username)** - checks if a username is banned in runescape.
  
        **?help** - calls this command.
        
        **could be deleted** - This message means the account with the checked username has never logged into rs3. Add the player ingame, if it fails then the name is either deleted or available to claim.
        """,
        colour = discord.Colour.gold()
    )
    await ctx.send(embed=embed)

client.run(token)
