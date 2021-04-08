from main import *
import discord
from discord.ext import commands
from replit import db
from datetime import datetime
import asyncio
from pytz import timezone
import embed

timeZones = ["EST", "PST", "MST", "GMT", "HST", "HST", "UTC"]

async def requirements(ctx, args):
	if ctx.author == client.user:
		pass

	if len(args) != 3:
		embedVar = embed.embed("Please enter a valid amount of arguements", "If you need help, please type ``a!help``.")
		await ctx.send(embed=embedVar)
		return False

	for argum in args:
		if argum == args[2]:
			continue
	
		if argum.isdigit() and not ":" in argum:
			embedVar = embed.embed("Please enter valid arguements", "If you need help, please type ``a!help``.")
			await ctx.send(embed=embedVar)
			return False

		argum = argum.replace(":", "")

		if argum.isdigit() and int(argum) > 1259 or argum.isdigit() and int(argum) < 100:
			embedVar = embed.embed("Please enter valid arguements", "If you need help, please type ``a!help``.")
			await ctx.send(embed=embedVar)
			return False

		if argum == args[1] and not argum.isdigit() and not argum.upper() in timeZones:
			embedVar = embed.embed("Please enter valid arguements", "If you need help, please type ``a!help``.")
			await ctx.send(embed=embedVar)
			return False

	if ctx.author.bot:
		return False

	return True

class events(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def settime(self, ctx, *args):
		if await requirements(ctx, args) == False:
			return

		embedVar = embed.embed("Time successfully set!", "Your time has successfully been set.")
		await ctx.send(embed=embedVar)
		

	async def test():
		while True:
			print('ehll iqjwfipoq')
			await asyncio.sleep(1)


	#client.loop.create_task(test())
	
mst = timezone('MST')
print("Time in MST:", datetime.now(mst))
 
est = timezone('EST')
print("Time in EST:", datetime.now(est))
 
utc = timezone('UTC')
print("Time in UTC:", datetime.now(utc))
 
gmt = timezone('GMT')
print("Time in GMT:", datetime.now(gmt))
 
hst = timezone('HST')
print("Time in HST:", datetime.now(hst))

def setup(client):
  client.add_cog(events(client))
