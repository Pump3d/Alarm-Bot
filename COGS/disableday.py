from main import *
import discord
from datetime import datetime, timedelta
from discord.ext import commands
from pytz import timezone
from replit import db
import tools

disdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

async def requirements(self, ctx, *args):
	try:
		db[str(ctx.guild.id)]
	except:
		embedVar = tools.embed("You have not set any alarms!", "Please type ``a!help`` to view command usage and how to set an alarm")
		await ctx.send(embed=embedVar)
		return

	if not ctx.message.author.guild_permissions.administrator:
		embedVar = tools.embed("You must be an admin!", "You must have the administrator role to use this command.")
		await ctx.send(embed=embedVar)
		return
	
	
	if tools.check(ctx.guild.id) == False:
		embedVar = tools.embed("You must set a channel before setting an alarm", "Please type ``a!setchannel [channel id]`` to set a channel for the bot to ping in.")
		await ctx.send(embed=embedVar) 
		return False
	
	if not args[1].lower().title() in disdays:
		embedVar = tools.embed("Please enter a valid day.", "Please enter a valid day of the week.")
		print("Not a valid day.")
		await ctx.send(embed=embedVar)
		return False
	
	if not args[0] in db[str(ctx.guild.id)]:
		embedVar = tools.embed("Not a valid Alarm ID.", "Please enter a valid alarm ID.")
		print("Not a valid Alarm ID.")
		await ctx.send(embed=embedVar)
		return False

	if args[1].lower().title() in db[str(ctx.guild.id)][args[0]]["disdays"]:
		embedVar = tools.embed("This day is already disabled for this alarm", "Please type ``a!help`` to view the command usage if you need help.")
		print("Date already in DB.")
		await ctx.send(embed=embedVar)
		return False

	db[str(ctx.guild.id)][args[0]]["disdays"].append(args[1].lower().title())
	return True
		


class events(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=["dsblday", "dd", "disabledate", "disable", "disab"])
	async def disableday(self, ctx, *args):

		req = await requirements(self, ctx, *args)
		if not req:
			return

		embedVar = tools.embed("Day successfully paused!", "This alarm will no longer send a notification on ``{}``.".format(args[1].lower().title()))
		await ctx.send(embed=embedVar)





def setup(client): 
	client.add_cog(events(client))