import os

import discord
from discord import Message
from discord.ext import commands

from dotenv import load_dotenv


load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message: Message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        await message.channel.send("test")


def main():
    bot.run(os.environ["DISCORD_KEY"])


if __name__ == "__main__":
    main()
