import discord
import json
import os
from discord.ext import commands

TOKEN = 'NTAzOTY0MzM4OTc4MjkxNzE5.DrDNyQ.Lzs6tW-x8peT8gocGzSY1LJ9CPI'

client = commands.Bot(command_prefix = '.')
client.remove_command('help')
os.chdir(r'C:\Users\Dan\Documents\CodingBots')

@client.event
async def on_message(message):
       author = message.author
       content = message.content
       print('{}: {}'.format(author, content))
       await client.process_commands(message)

@client.event
async def on_ready():
         await client.change_presence(game=discord.Game(name= 'RoarBot'))
         print('Bot is ready beep boop beep')

@client.command()
async def roar():
    await client.say('ROAR!')

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def amisexy():
    await client.say('Of Course You Are The Sexiest Man On Earth')

@client.command()
async def Dino():
    await client.say(':RoarBot:')



@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='roar', value='Replies To Your Message Saying ROAR!', inline=False)
    embed.add_field(name='ping', value='Replies To Your Message Saying Pong!', inline=False)
    embed.add_field(name='iamsexy', value='Replies Making You Feel All Warm Inside', inline=False)

    await client.send_message(author, embed=embed)

client.run(TOKEN)
