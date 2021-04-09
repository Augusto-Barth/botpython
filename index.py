import os
import discord
from dotenv import load_dotenv
import json
import random
# from dict import comandos

# importar token de config.json, mas agora uso .env
data = open('links.json', "r")
links = json.load(data)

# importando o .env, para utilizar o token do bot e a lista de comandos simples
load_dotenv()
btoken = os.getenv('token')
prefix = os.getenv('prefix')
response_object = links

# pemitindo o bot ver outras pessoas, e mais algumas coisas da API que eu com certeza entendo
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)


# função para tratar o input dos comandos, separando o prefixo dos comandos e dos argumentos(caso haja algum)
def trata_argumentos(message):
    args = message.content[len(prefix):]
    args2 = args.strip().split()
    argumentoslist = str(args2[1:]).lower()
    comandolist = str(args2[:1]).lower()
    comando = "".join(str(x) for x in comandolist)[2:len(comandolist) - 2]
    argumentos = "".join(str(x) for x in argumentoslist)[2:len(argumentoslist) - 2]
    return comando, argumentos


@client.event
async def on_ready():
    print('Conectado como {0.user}'.format(client))
    await client.change_presence(activity=discord.Game('"!comandos" para ajuda'))
    print('Bot foi iniciado, com {} usuários, em {} servers.' .format(len(client.users), len(client.guilds)))


@client.event
async def on_message(message):
    if message.author.bot:
        return

    # pequena função anônima para encurtar a mesma função de sempre
    manda = lambda mens: message.channel.send('{}'.format(mens))

    if message.content.startswith(prefix):
        comando, argumentos = trata_argumentos(message)

        if comando == 'ping':
            await manda(comando)

        elif comando == 'roleta':
            n = random.randint(0, 1)
            if n == 0:
                await manda('Morreu!')
            else:
                await manda('Sobreviveu!')

    if message.content in response_object:
        await manda(response_object[message.content])

    if ';-;' in message.content:
        await manda(';-;')

client.run(btoken)

