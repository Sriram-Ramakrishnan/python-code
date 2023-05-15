import os

import discord

TOKEN = "Nzk3MTA0MTIxNzczMjkzNTY4.X_hnEA.Ph4x_NMe4tFTIKcRtPyVGinmOAg"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
    if message.content.lower() == "hello":
        await message.channel.send(".menu")

client.run(TOKEN)
