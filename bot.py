# Alright, Lets import all the stuff we need to run the bot.
import discord
import sys
import time
from discord.ext.commands import Bot
from discord.ext import commands
# Great! Everything is imported, now we chose our prefix, to do this change the $ below to whatever you want the bot to recognize as a prefix.
# DO NOT REMOVE THE '', Just change the dollar sign to somthing else :)
bot = commands.Bot(command_prefix= '$')

# Great! The bots online, this is now a event. It will print to the console that the bot is online
@bot.event
async def on_ready():
    #These are all the actions that are provided after the bot is online.
    print('Connected to discord as: {0.user}'.format(bot))
    # Changes the presence of the bot to say "Watching humans"
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="humans"))
    # Theres better ways of printing how many servers your in, but this works.
    print('I am the following number of servers')
    print({len(bot.guilds)})

#Great theres a message that begins with a $, lets check if its meant for us.
@bot.command()
async def test(ctx):
    # Seems like it is! Lets send back a message!
    await ctx.send('Hello!')
    # We sent back a message, lets countinue on listening for commands!

print("Connecting to discord...")
bot.run('TOKEN GOES HERE')
