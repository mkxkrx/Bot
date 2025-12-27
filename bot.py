import discord
from discord.ext import commands

TARGET_USER_ID = 123456789012345678  # user to copy
TOKEN = "YOUR_BOT_TOKEN"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    # Ignore bots (including itself)
    if message.author.bot:
        return

    # Check target user
    if message.author.id == 1340356256120045589:
        # Send modified message
        await message.channel.send(message.content + "~")

        # Optional: delete original message
        # await message.delete()

    await bot.process_commands(message)

bot.run(TOKEN)
