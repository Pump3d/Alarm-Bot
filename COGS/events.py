from main import *
import discord
from discord.ext import commands
from replit import db
import tools

class events(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	
	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		for channel in guild.text_channels:
			if channel.permissions_for(guild.me).send_messages:
					embedVar = tools.embed("Thank you for adding me to your server", "Please type ``a!help`` to view the command usage.")
					await channel.send(embed=embedVar)
					break
	
	@commands.Cog.listener()
	async def on_guild_remove(self, guild):
		if tools.check(guild.id):
			del db[str(guild.id)]


def setup(client):
  client.add_cog(events(client))

