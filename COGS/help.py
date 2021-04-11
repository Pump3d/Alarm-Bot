from main import *
import discord
from discord.ext import commands
from replit import db
import tools


class events(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def help(self, ctx, *args):
		embedVar = tools.embed("Alarm Bot Help", "``a!help``: This message. \n ``a!settime``: Set the time you want for ping. \n ``a!credits``: Displays the credits.") 
		await ctx.send(embed=embedVar)
		
	@commands.command()
	async def timezones(self, ctx, *args):
		embedVar = tools.embed("Compatible Timezones", "``EST``: Eastern Standard Time \n ``PST``: Pacific Standard Time \n ``MST``: Mountain Standard Time \n ``GMT``: Greenwich Mean Time \n ``HST``: Hawaii Standard Time \n ``UTC``: Coordinated Universal Time \n ``CT``: Central Time \n ``Troll``: Troll")
		await ctx.send(embed=embedVar)

	@commands.command()
	async def credits(self, ctx, *args):
		embedVar = tools.embed("Credits", "Bot made by ChillPanda and Pump3d.")
		await ctx.send(embed=embedVar)

#["EST", "PST", "MST", "GMT", "HST", "HST", "UTC"]
	
def setup(client):
  client.add_cog(events(client))
