from main import *
import discord
from discord.ext import commands
from replit import db
import tools

async def requirements(ctx, args):
	if len(args) > 1:
		embedVar = tools.embed()
		await ctx.send(embed=embedVar)
		return

class events(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def setrole(self, ctx, *args):
		if requirements == False:
			embedVar = tools.embed()
			await ctx.send(embed=embedVar)


def setup(client):
  client.add_cog(events(client))

