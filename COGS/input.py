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

	
	if ctx.author.bot:
		return False
	
	
	for argum in args:
		if argum == args[3]:
			continue #im gonna print to see whats stopping it

		print(args[0], args[1], args[2], args[3])
		if argum.isdigit() and not ":" in argum:
			print("Time doesnt have colon")
			embedVar = tools.embed("Please enter valid arguements", "If you need help, please type ``a!help``.")
			await ctx.send(embed=embedVar)
			return False 

		argum = argum.replace(":", "")

		if argum.isdigit() and int(argum) > 1259 or argum.isdigit() and int(argum) < 100:
			print("Time too long / short")
			embedVar = tools.embed("Please enter valid arguements", "If you need help, please type ``a!help``.")
			await ctx.send(embed=embedVar)
			return False

		if argum == args[2] and not argum.upper() in timeZones:
			print("Not a valid timezone")
			embedVar = tools.embed("Please enter valid arguements", "If you need help, please type ``a!help``.")
			await ctx.send(embed=embedVar)
			return False

		if argum == args[1] and argum != "AM" and argum != "PM": 
			print("Not AM or PM") # it hmm i see lol same dumb mistake i made last time
			embedVar = tools.embed("Please enter valid arguements", "If you need help, please type ``a!help``.")
			await ctx.send(embed=embedVar) 
			return False #add Added AM/PM or something for the comment

	name = " ".join(args)
	
	if tools.check(ctx.guild.id) == False:
		db[str(ctx.guild.id)] = {name: {"time": args[0], "apm": args[1], "timezone": args[2],"name": args[3]}}
		#self.client.loop.create_task(cooldown(str(ctx.guild.id))) wait we already 
	else:
		db[str(ctx.guild.id)] = {name: {"time": args[0], "apm": args[1], "timezone": args[2],"name": args[3]}}
		
	for tz in timeZones:
		tz = timezone(timeZones[tz])
		date = datetime.now(tz)
		date = date.strftime("%-I:%M %p")
		print(date)
		
		print(args[0], args[1], args[2], args[3])

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
