import os

import discord

TOKEN = "Enter your token here"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
    if message.content.lower() == "hello":
        await message.channel.send(".menu")

client.run(TOKEN)
