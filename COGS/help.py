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
		embedVar = tools.embed("Alarm Bot Help", "``a!help``: This message. \n ``a!settime [Hours:Minutes AM/PM Timezone Message]``: Set an alarm (stackable). \n ``a!timezones``: Displays the compatible timezones. \n ``a!setchannel``: Sets the channel for alarm. \n ``a!setrole``: Role ID \n ``a!deletealarm``: Delete a certain alarm that was set. \n ``a!credits``: Displays the credits.") 
		await ctx.send(embed=embedVar)
		
	@commands.command()
	async def timezones(self, ctx, *args):
		embedVar = tools.embed("Compatible Timezones", "``EST``: Eastern Standard Time \n ``PST``: Pacific Standard Time \n ``MST``: Mountain Standard Time \n ``GMT``: Greenwich Mean Time \n ``HST``: Hawaii Standard Time \n ``UTC``: Coordinated Universal Time \n ``CT``: Central Time \n ``Troll``: Troll")
		await ctx.send(embed=embedVar)

	@commands.command()
	async def credits(self, ctx, *args):
		embedVar = tools.embed("Credits", "Bot made by ``ChillPanda#5842`` and ``Pump3d#3682``.")
		await ctx.send(embed=embedVar)

#["EST", "PST", "MST", "GMT", "HST", "HST", "UTC"]
	
def setup(client):
  client.add_cog(events(client))
