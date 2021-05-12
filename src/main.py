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
    print(f'{client.user.name} beep bop!')


@client.event
async def on_member_join(member):

    new_member_dm = member.dm_channel

    if new_member_dm is None:
        await member.create_dm()
        new_member_dm = member.dm_channel
    try:
        await member.send(welcome_message_data
                          .format(new_member_name=member.name))
    except Exception as e:
        print(e)


client.run(TOKEN)
