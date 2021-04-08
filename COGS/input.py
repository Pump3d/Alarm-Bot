from main import *
import discord
from discord.ext import commands
from replit import db
from datetime import datetime
import asyncio
from pytz import timezone
import tools

timeZones = {
"EST": "US/EASTERN",
"PST": "US/PACIFIC",
"MST": "US/MOUNTAIN",
"GMT": "Etc/GMT",
"HST": "US/HAWAII",
"UTC": "Etc/Universal",
"CT": "US/CENTRAL",
"Universal": "Universal",
"Troll": "Antarctica/Troll"
}

async def requirements(ctx, args):
	if ctx.author == client.user:
		pass

	if len(args) != 3:
		embedVar = tools.embed("Please enter a valid amount of arguements", "If you need help, please type ``a!help``.")
		await ctx.send(embed=embedVar)
		return False

	for argum in args:
		if argum == args[2]:
			continue
	
		if argum.isdigit() and not ":" in argum:
			embedVar = tools.embed("Please enter valid arguements", "If you need help, please type ``a!help``.")
			await ctx.send(embed=embedVar)
			return False

		argum = argum.replace(":", "")

		if argum.isdigit() and int(argum) > 1259 or argum.isdigit() and int(argum) < 100:
			embedVar = tools.embed("Please enter valid arguements", "If you need help, please type ``a!help``.")
			await ctx.send(embed=embedVar)
			return False

		if argum == args[1] and not argum.isdigit() and not argum.upper() in timeZones:
			embedVar = tools.embed("Please enter valid arguements", "If you need help, please type ``a!help``.")
			await ctx.send(embed=embedVar)
			return False

		name = " ".join(args)
		if tools.check(ctx.guild.id) == False:
			db[str(ctx.guild.id)] = {name: {"time": args[0], "apm": args[1], "name": args[2]}}
			client.loop.create_task(cooldown(str(ctx.guild.id)))
		else:
			db[str(ctx.guild.id)] = {name: {"time": args[0], "apm": args[1], "name": args[2]}}

	if ctx.author.bot:
		return False

	return True

async def cooldown(guild):
	while True:
		for date in sorted(db[guild].items()):
			if datetime.now().strftime("%H:%M"): 
				await asyncio.sleep(60)

for tz in timeZones:
	tz = timezone(timeZones[tz])
	date = datetime.now(tz)
	date = date.strftime("%-I:%M %p")
	print(date)

class events(commands.Cog):
	def __init__(self, client):
		self.client = client

	
	@commands.command()
	async def settime(self, ctx, *args):
		if await requirements(ctx, args) == False:
			return

		embedVar = tools.embed("Time successfully set!", "Your time has successfully been set.")	
		await ctx.send(embed=embedVar)
	

def setup(client):
  client.add_cog(events(client))
