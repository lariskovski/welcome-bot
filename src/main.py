import os
import discord

intents = discord.Intents.default()
intents.members = True

TOKEN = os.getenv('API_TOKEN')

client = discord.Client(intents=intents)

with open('./welcome-message.md', 'r') as file:
    welcome_message_data = file.read()


@client.event
async def on_ready():
    print(f'{client.user.name} ta ON!')


@client.event
async def on_member_join(member):

    joined_user_dm = member.dm_channel

    if joined_user_dm is None:
        await member.create_dm()
        joined_user_dm = member.dm_channel
    try:
        await member.send(welcome_message_data)
    except Exception as e:
        print(e)


client.run(TOKEN)
