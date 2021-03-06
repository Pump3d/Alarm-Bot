import discord
import os
import discord.ext
import asyncio
from discord.utils import get, find
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import keep_alive

client = discord.Client() 
client = commands.Bot(help_command = None, command_prefix = 'a!')

@client.event
async def on_ready():
	keep_alive.keep_alive()
	print("bot online")
	game = discord.Game("a!help")
	await client.change_presence(status=discord.Status.online, activity=game)


for file in os.listdir('./COGS'):
	if file.endswith(".py"):
		client.load_extension(f'COGS.{file[:-3]}')
		print(file[:-3] + " has loaded")

client.run(os.getenv('TOKEN'))