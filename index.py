import os
import discord
from dotenv import load_dotenv
import json
#importar token de config.json, mas agora uso .env

data = open('links.json', "r")
links = json.load(data)

load_dotenv()
btoken = os.getenv('token')
prefix = os.getenv('prefix')
response_object = links

client = discord.Client()


@client.event
async def on_ready():
    print('Conectado como {0.user}'.format(client))
    await client.change_presence(activity=discord.Game('"!comandos" para ajuda'))
    # print('Bot foi iniciado, com {0} usuários, em {1} canais de {2} servers.' .format(client.user.size, client.channels.size, client.guilds.size))


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith(prefix):
        args = message.content[len(prefix):]
        args2 = args.strip().split()
        comando = str(args2[1:]).lower()

        if comando == 'teste':
            await message.channel.send('testado!')

    if message.content in response_object:
        await message.channel.send(response_object[message.content])


client.run(btoken)
