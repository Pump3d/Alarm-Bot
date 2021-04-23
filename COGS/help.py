from main import *
import discord
from discord.ext import commands
from replit import db
import tools
from COGS.setalarm import timeZones

class events(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def help(self, ctx, *args):
		embedVar = tools.embed("Alarm Bot Help", "``a!help``: This message. \n ``a!settime [Hours:Minutes AM/PM Timezone Role-ID Message]``: Set an alarm (stackable). \n ``a!timezones``: Displays the compatible timezones. \n ``a!setchannel``: Sets the channel for alarm. \n ``a!setrole``: Role ID \n ``a!alarms``: Shows all the current server alarms and their IDs. \n ``a!remove [Alarm Id]``: Delete a certain alarm that has been set. \n ``a!disableday``: Set a day where a certain alarm will NOT send a message. \n ``a!enableday``: Resume a day that was paused. \n ``a!credits``: Displays the credits.") 
		await ctx.send(embed=embedVar)
		
	@commands.command(aliases=["tz", "timezone"])
	async def timezones(self, ctx, *args):
		string = ""
		for tz in timeZones:
			string = string + "``{}``: ".format(tz) + timeZones[tz] + "\n"


		embedVar = tools.embed("Compatible Timezones", string)
		await ctx.send(embed=embedVar)

	@commands.command()
	async def credits(self, ctx, *args):
		embedVar = tools.embed("Credits", "Bot made by ``ChillPanda#5842`` and ``Pump3d#3682``. Special thanks to ``mege#0951`` for making the profile picture.")
		await ctx.send(embed=embedVar)

	@commands.command()
	async def alarms(self, ctx):
		try:
			db[str(ctx.guild.id)]
		except:
			embedVar = tools.embed("You have not set any alarms!", "Please type ``a!help`` to view command usage and how to set an alarm")
			await ctx.send(embed=embedVar)
			return

		string = ""
		for elem in db[str(ctx.guild.id)]:
			if elem == "channel":
				continue

			string = string + "**{}**".format(db[str(ctx.guild.id)][elem]["name"]) + ":\n ㅤ Time: ``{} {} {}`` ".format(db[str(ctx.guild.id)][elem]["time"], db[str(ctx.guild.id)][elem]["apm"], db[str(ctx.guild.id)][elem]["timezone"])  + "\nㅤ  ID: ``{}`` \n".format(elem)

		if string == "":
			embedVar = tools.embed("You have not set any alarms!", "Please type ``a!help`` to view command usage and how to set an alarm")
			await ctx.send(embed=embedVar)
			return

		embedVar = tools.embed("Server Alarms", string)
		await ctx.send(embed=embedVar)


def setup(client):
  client.add_cog(events(client))
