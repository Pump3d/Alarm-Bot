from main import *
import discord
from discord.ext import commands
from replit import db
from datetime import datetime, timedelta
import asyncio
from pytz import timezone
import tools
import time


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

async def cooldown(guild):
	while True:
		t0 = time.time()

		for date in sorted(db[guild].items()):
			date = date[1]
			if datetime.now(timezone(timeZones[date["timezone"]])).strftime("%-I:%M%p") == date["time"] + date["apm"]: 
				print("e") 
			else:
				print("Not time yet") 

		t1 = time.time()

		await asyncio.sleep((60 - datetime.utcnow().second) - (t1 - t0)) 

async def requirements(self, ctx, args):
	if ctx.author.id == "771153822994530354" or ctx.author.id == "696790718743838793":
		print("hi")

	
	if ctx.author.bot:
		return False
	
	if len(args) < 5:
		print("Too little arguements")
		embedVar = tools.embed("Please enter a valid amount of arguments", "If you need help, please type ``a!help``.")
		await ctx.send(embed=embedVar)
		return False
	
	if args[0] and not ":" in args[0]:
		print("Time doesnt have colon")
		embedVar = tools.embed("Please enter a valid time", "If you need help, please type ``a!help``.")
		await ctx.send(embed=embedVar)
		return False 

	if args[0] and len(args[0].split(":")[1]) < 2:
		print("Minutes is too short")
		embedVar = tools.embed("Please enter a valid time", "If you need help, please type ``a!help``.")
		await ctx.send(embed=embedVar)
		return False 

	arg0int = args[0].replace(":", "")

	if arg0int.isdigit() and int(arg0int) > 1259 or arg0int.isdigit() and int(arg0int) < 100:
		print("Time too long / short")
		embedVar = tools.embed("Please enter a valid time", "If you need help, please type ``a!help``.")
		await ctx.send(embed=embedVar)
		return False

	if args[2] and not args[2].upper() in timeZones:
		print("Not a valid timezone")
		embedVar = tools.embed("Please enter compatible timezone (a!timezones)", "If you need help, please type ``a!help``.")
		await ctx.send(embed=embedVar)
		return False
	
	if args[1] and args[1] != "AM" and args[1] != "PM": 
		print("Not AM or PM") 
		embedVar = tools.embed("Please enter AM or PM as a valid argument", "If you need help, please type ``a!help``.")
		await ctx.send(embed=embedVar) 
		return False 


	if not discord.utils.get(ctx.message.guild.roles, id=int(args[3])):
		print("Invalid role") 
		embedVar = tools.embed("Please enter a valid role ID", "If you need help, please type ``a!help``.")
		await ctx.send(embed=embedVar) 
		return False 


	almName = " ".join(args)
	name = None

	for x in range(4, len(args)):
		if name == None:
			name = args[x]
			continue

		name = name + " " + args[x]

	print(name)

	if tools.check(ctx.guild.id) == False:
		db[str(ctx.guild.id)] = {}
		db[str(ctx.guild.id)][almName] = {"time": args[0], "apm": args[1], "timezone": args[2], "role": args[3], "name": name}
		
		self.client.loop.create_task(cooldown(str(ctx.guild.id)))

	else:
		db[str(ctx.guild.id)][almName] = {"time": args[0], "apm": args[1], "timezone": args[2], "role": args[3], "name": name}
	
		self.client.loop.create_task(cooldown(str(ctx.guild.id)))

	return True

for tz in timeZones:
	tz = timezone(timeZones[tz])
	date = datetime.now(tz)
	date = date.strftime("%-I:%M %p")
	print(date)

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
		if await requirements(self, ctx, args) == False:
			return

		embedVar = tools.embed("Time successfully set!", "Your time has successfully been set.")	
		await ctx.send(embed=embedVar)
	

def setup(client):
  client.add_cog(events(client))
