import discord
import os
import discord.ext
from discord.utils import get, find
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check

client = discord.Client()
client = commands.Bot(help_command = None, command_prefix = 'a!')

@client.event
async def on_ready():
  print("bot online")

for file in os.listdir('./COGS'):
	if file.endswith(".py"):
		client.load_extension(f'COGS.{file[:-3]}')
		print(file[:-3] + " has loaded")

client.run(os.getenv('TOKEN'))