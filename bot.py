import discord #Импортируем библиотеку "disnake" // Import the "disnake" library
from disnake.ext import commands
from config import settings

class TestBot(commands.Bot):
    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print("Запущен!")

intents = disnake.Intents.all()
bot = MyBot(command_prefix=settings['PREFIX'], intents = intents) #Ваш префикс бота (по умолчанию префикс "!") // Your bot prefix (default prefix "!")

@bot.command()
async def test(ctx):
	await ctx.send("Привет! // Hello!")
	print("Тест команда была успешно выполнена // The test command has been executed")

 # Токен бота можно получить на https://discord.com/developers/applications // Bot token available at https://discord.com/developers/applications
bot.run(settings['TOKEN'])
