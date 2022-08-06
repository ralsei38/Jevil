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
                    await self._ping(message)
                elif 'grade' in message.content:
                    await self._grade(message)


        def _grade(self, message):
            with requests.Session() as session:
                    session.auth = (os.getenv('CHAMILO_USERNAME'), os.getenv('CHAMILO_PASSWORD'))
                    result = session.get("https://cas-uga.grenet.fr/login")
                    result = session.post("https://cas-uga.grenet.fr/login")
                    result = session.get("https://scolarite-informatique.iut2.univ-grenoble-alpes.fr/app/erreur.php") #page down pour le moment ;-;
                    print(result.text)
        
        def _ping(self, message):
            return message.channel.send("pong")

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD_ID = os.getenv('DISCORD_GUILD')
    bot = Jevil()
    bot.run(TOKEN)