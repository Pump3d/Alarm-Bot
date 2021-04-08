from main import *
import discord
from discord.ext import commands
from replit import db


class events(commands.Cog):
	def __init__(self, client):
		self.client = client
	


def setup(client):
  client.add_cog(events(client))

