import discord
import logging
logging.basicConfig(level=logging.INFO)
import re
import rollerSkeleton
from E3EBOT_TOKEN import BOT_TOKEN
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(BOT_TOKEN)
