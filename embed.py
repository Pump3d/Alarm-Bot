import discord

colorVar = 0xc91414

def embed(header, desc):
	embedVar = discord.Embed(title = header, description = desc, color = colorVar)
	return embedVar