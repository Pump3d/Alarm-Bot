from main import *
import discord
from discord.ext import commands
from replit import db
import embed


class events(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def help(self, ctx, *args):
		embedVar = embed.embed("Alarm Bot Help", "``a!help``: This message. \n ``a!settime``: Set the time you want for ping.") 
		await ctx.send(embed=embedVar)


	
def setup(client):
  client.add_cog(events(client))
