import discord
from replit import db

colorVar = 0xBE1931

def embed(header, desc):
	embedVar = discord.Embed(title = header, description = desc, color = colorVar)
	return embedVar

def check(name):
	try:
		db[str(name)]
		return True
	except:
		return False 
