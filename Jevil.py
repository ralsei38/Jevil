import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging
import requests

class Jevil(commands.Bot):
        def __init__(self):
            super().__init__('$')
            logging.basicConfig(level=logging.INFO) #filename='discord.log'
        
        async def on_ready(self) -> None:
            logging.info(f"{self.user} has connected to discord !")
        
        async def on_message(self, message) -> str:
            if message.content.startswith('!'):
                if 'ping' in message.content:
                    await _ping(message)
        
        def _grade(self, message):
            with requests.Session() as session:
                    session.auth = ('username', getpass())

        def _ping(self, message):
            return message.channel.send("pong")

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD_ID = os.getenv('DISCORD_GUILD')
    bot = Jevil()
    bot.run(TOKEN)