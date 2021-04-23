from main import *
import discord
from discord.ext import commands
from replit import db
from datetime import datetime, timedelta
import asyncio
from pytz import timezone
import tools

tasking = []

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

async def cooldown(self, guild):
	tasking.append(guild)
	await self.client.wait_until_ready()
	while True:

		if not tools.check(guild):
			break

		for date in sorted(db[guild].items()):
			if date[0] == "channel":
				continue

			date = date[1]

			tz = timezone(timeZones[date["timezone"]])
			day = datetime.now(tz)
			day = day.strftime("%A")

			if not day in date["disdays"]:
				if datetime.now(timezone(timeZones[date["timezone"]])).strftime("%-I:%M%p") == date["time"] + date["apm"]: 
					embedVar = tools.embed("Alarm", "<@&" + str(date["role"]) + "> " + date["name"])
					channel = self.client.get_channel(db[guild]["channel"])
					await channel.send(embed=embedVar)
					mention = await channel.send("<@&" + str(date["role"]) + ">")
					await mention.delete()

		await asyncio.sleep((60 - datetime.utcnow().second) + 3) 


def activate(self):
	for guild in db.keys():
		self.client.loop.create_task(cooldown(self, guild))


async def requirements(self, ctx, args):
	if not ctx.message.author.guild_permissions.administrator:
		embedVar = tools.embed("You must be an admin!", "You must have the administrator role to use this command.")
		await ctx.send(embed=embedVar)
		return

	if ctx.author.id == "771153822994530354" or ctx.author.id == "696790718743838793":
		print("hi")

	
	if ctx.author.bot:
		return False
	
	if len(args) < 5:
		print("Too little arguements")
		embedVar = tools.embed("Please enter a valid amount of arguments", "Please check ``a!help`` to see the bot command usage.")
		await ctx.send(embed=embedVar)
		return False
	
	if args[0] and not ":" in args[0]:
		print("Time doesnt have colon")
		embedVar = tools.embed("Please enter a valid time", "Please enter a valid time using the ``hour:format`` method.")
		await ctx.send(embed=embedVar)
		return False 

	if args[0] and len(args[0].split(":")[1]) != 2:
		print("Minutes is too short")
		embedVar = tools.embed("Please enter a valid time", "Please enter a valid arguement for the number of minutes.")
		await ctx.send(embed=embedVar)
		return False 

	arg0int = args[0].replace(":", "")

	if arg0int.isdigit() and int(arg0int) > 1259 or arg0int.isdigit() and int(arg0int) < 100:
		print("Time too long / short")
		embedVar = tools.embed("Please enter a valid time", "Please enter a valid time using standard clock format.")
		await ctx.send(embed=embedVar)
		return False

	if args[2] and not args[2].upper() in timeZones:
		print("Not a valid timezone")
		embedVar = tools.embed("Please enter a compatible timezone", "To view the list of compatible timezones, please type ``a!timezones``.")
		await ctx.send(embed=embedVar)
		return False
	
	if args[1] and args[1].upper() != "AM" and args[1].upper() != "PM": 
		print("Not AM or PM") 
		embedVar = tools.embed("Please enter AM or PM as a valid argument", "Please enter a valid time using standard clock format.")
		await ctx.send(embed=embedVar) 
		return False 

	try:
		int(args[3])
	except:
		embedVar = tools.embed("Please enter a valid role ID", "Please enter a valid role id, and do not use mentions.")
		await ctx.send(embed=embedVar) 
		return False

	if not discord.utils.get(ctx.message.guild.roles, id=int(args[3])):
		print("Invalid role") 
		embedVar = tools.embed("Please enter a valid role ID", "Please enter a valid role id, and do not use mentions.")
		await ctx.send(embed=embedVar) 

	if tools.check(ctx.guild.id) == False:
		embedVar = tools.embed("You must set a channel before setting an alarm", "Please type ``a!setchannel [channel id]`` to set a channel for the bot to ping in.")
		await ctx.send(embed=embedVar) 
		return False


	name = None

	for x in range(4, len(args)):
		if name == None:
			name = args[x]
			continue

		name = name + " " + args[x]

	for date in sorted(db[str(ctx.guild.id)].items()):
		if date[0] == "channel":
			continue

		date = date[1]
		if date["name"] == name:
			embedVar = tools.embed("There is already an alarm with the same name!", "Please use ``a!deletealarm`` to delete the previous alarm before setting a new one.")
			await ctx.send(embed=embedVar) 
			return False

	db[str(ctx.guild.id)][str(ctx.message.id)] = {"time": args[0], "apm": args[1], "timezone": args[2], "role": int(args[3]), "name": name, "disdays": []}
	
	if not str(ctx.guild.id) in tasking:	
		self.client.loop.create_task(cooldown(self, str(ctx.guild.id)))

	return str(ctx.message.id)


for tz in timeZones:
	tz = timezone(timeZones[tz])
	date = datetime.now(tz)
	date = date.strftime("%-I:%M %p")
	print(date)

class events(commands.Cog):

	def __init__(self, client):
		self.client = client
		activate(self)

	
	@commands.command(aliases=["setalarm", "sa"])
	async def settime(self, ctx, *args):
		req = await requirements(self, ctx, args)
		if not req:
			return

		embedVar = tools.embed("Time successfully set!", "Your time has successfully been set.")
		embedVar.set_footer(text="Alarm ID: {}".format(req))
		await ctx.send(embed=embedVar)


def setup(client):
  client.add_cog(events(client))

