from main import *
import discord
from discord.ext import commands
from replit import db
import tools

async def requirements(ctx, args):
	if ctx.author.bot:
		return False

	if len(args) > 1:
		embedVar = tools.embed("Please enter a valid role", "If you need help, please type ``a!help``.")
		await ctx.send(embed=embedVar)
		return False

class events(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def setchannel(self, ctx, *args): 
			if not ctx.message.author.guild_permissions.administrator:
				embedVar = tools.embed("You must be an admin!", "You must have the administrator role to use this command.")
				await ctx.send(embed=embedVar)
				return

			
			id = ''.join(args)
			channel = None
			try:
				channel = self.client.get_channel(int(id))
			except:
				embedVar = tools.embed("Invalid channel ID", "Please enter a valid channel ID.")
				await ctx.send(embed=embedVar)
				return

			if channel == None:
				embedVar = tools.embed("Invalid channel ID", "Please enter a valid channel ID.")
				await ctx.send(embed=embedVar)
			else:
				for channel in ctx.message.guild.channels:
					if channel == self.client.get_channel(int(id)):
						db[str(ctx.guild.id)]["channel"] = int(id)
						embedVar = tools.embed("Successfully set channel", "Your channel has been successfully set.")
						await ctx.send(embed=embedVar)
						return
				
				embedVar = tools.embed("Invalid channel ID", "If you need help, please type ``a!help``.")
				await ctx.send(embed=embedVar)

	@commands.command()
	async def remove(self, ctx, args):
		
		pass


def setup(client):
  client.add_cog(events(client))
