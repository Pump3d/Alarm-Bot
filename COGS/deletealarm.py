from main import *
import discord
from discord.ext import commands
from replit import db
import tools

async def requirements(self, ctx, args):
	if not ctx.message.author.guild_permissions.administrator:
		embedVar = tools.embed("You must be an admin!", "You must have the administrator role to use this command.")
		await ctx.send(embed=embedVar)
		return

	if not args:
		embedVar = tools.embed("Please enter a valid arguement", "You have not entered any arguements.")
		await ctx.send(embed=embedVar)
		return False

	if not tools.check(ctx.guild.id):
		embedVar = tools.embed("You have not set any alarms!", "Please type ``a!help`` for help on how to create one.")
		await ctx.send(embed=embedVar)
		return False

	args = " ".join(args)
	for date in sorted(db[str(ctx.guild.id)].items()):
		if date[0] == "channel":
			continue

		date2 = date[1]
		
		if args == date2["name"]:
			del db[str(ctx.guild.id)][date[0]]
			embedVar = tools.embed("Successfully deleted alarm", "Alarm ``" + date2["name"] + "`` has been successfully deleted.")
			await ctx.send(embed=embedVar)
			return


	embedVar = tools.embed("Could not find alarm", "Alarm ``" + args + "`` does not exist.")
	await ctx.send(embed=embedVar)
		

	
	

class events(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def deletealarm(self, ctx, *args):
		if await requirements(self, ctx, args) == False:
			return
	


def setup(client):
  client.add_cog(events(client))

