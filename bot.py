import discord #Импортируем библиотеку "discord" // Import the "discord" library
from discord.ext import commands

#Ваш префикс бота (по умолчанию префикс "!") // Your bot prefix (default prefix "!")
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
	print("Bot Ready!")

@bot.command()
async def test(ctx):
	await ctx.send("Привет! // Hello!")
	print("The test command has been executed ✔")

bot.run("Ваш токен бота // You Bot Token")
