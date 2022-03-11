# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

import scheduler

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ROLE_ID = int(os.getenv('ROLE_ID'))
MESSAGE_TO_REACT_ID = int(os.getenv('REACT_MSG_ID'))
CHANNEL_ID = str(os.getenv('CHANNEL_ID'))

EMOJI_TO_GAIN_REACT_ROLE = '👀'

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_raw_reaction_add(payload):
	if payload.message_id == MESSAGE_TO_REACT_ID and payload.emoji.name == EMOJI_TO_GAIN_REACT_ROLE:
		member = payload.member
		role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id = ROLE_ID)
		await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
	if payload.message_id == MESSAGE_TO_REACT_ID and payload.emoji.name == EMOJI_TO_GAIN_REACT_ROLE:
		member = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id)
		role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id = ROLE_ID)
		await member.remove_roles(role)

@bot.command(name="work", help="Alerts you in 20 minutes.")
async def work_function(ctx):
	if [role.id for role in ctx.author.roles]:
		scheduler.scheduleDM(ctx.author, "!work is now available! <#" + CHANNEL_ID + ">", 20*60)

@bot.command(name="daily", help="Alerts you in 20 hours.")
async def daily_function(ctx):
	if [role.id for role in ctx.author.roles]:
		scheduler.scheduleDM(ctx.author, "!daily is now available! <#" + CHANNEL_ID + ">", 20*60*60)

@bot.command(name="vote", help="Alerts you in 12 hours.")
async def vote_function(ctx):
	if [role.id for role in ctx.author.roles]:
		scheduler.scheduleDM(ctx.author, "!vote is now available! <#" + CHANNEL_ID + ">", 12*60*60)

@bot.command(name="custom", help="Sets a custom timer and alerts you. Usage: !custom <minutes> <seconds>")
async def custom_function(ctx, minutes_set, seconds_set=0):
	if [role.id for role in ctx.author.roles]:
		scheduler.scheduleDM(ctx.author, "Custom timer is finished! <#" + CHANNEL_ID + ">", int(minutes_set)*60 + seconds_set)

bot.run(TOKEN)