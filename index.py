import discord
import json
import random
# from dict import comandos

# importar token de config.json, mas agora uso .env
data = open('links.json', "r")
links = json.load(data)

# importando o .env, para utilizar o token do bot e a lista de comandos simples
# não uso mais .env porque e mais facil utilizar json
# load_dotenv()
# btoken = os.getenv('token')
# prefix = os.getenv('prefix')

# importando o token por um json
conf = open('config.json', "r")
confs = json.load(conf)
btoken = confs['token']

response_object = links

# colocando o prefixo no próprio arquivo, porque eu nao sei mexer no git
prefix = '!'

# pemitindo o bot ver outras pessoas, e mais algumas coisas da API que eu com certeza entendo
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

# lista de jogos para a roleta game
games = ['Lolzin', 'Cszin', 'Stardew Valley', 'Outro']

# pepemonkas = [emoji for emoji in client.emojis if client.emoji.name == "pepemonkas"]
pepemonkas = '<:pepemonkas:622174234352812052>'


# funcao para tratar o input dos comandos, separando o prefixo dos comandos e dos argumentos(caso haja algum)
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

    # pequena funcao anônima para encurtar a mesma funcao de sempre
    manda = lambda mens: message.channel.send('{}'.format(mens))

    if message.content.startswith(prefix):
        comando, argumentos = trata_argumentos(message)

        if comando == 'ping':
            pingm = await manda('Ping?')
            await pingm.edit(content = 'Pong! Latência de {0} ms. Latência de API {1} ms'.format(str(pingm.created_at - message.created_at)[8:-3], round(client.latency*1000)))

        elif comando == 'roleta' and argumentos == "":
            n = random.randint(0, 1)
            if n == 0:
                await manda('Morreu!')
            else:
                await manda('Sobreviveu!')

        elif comando == 'roleta' and argumentos == "role":
            n = random.randint(0, 4)
            if n == 0:
                await manda('Top!')
            elif n == 1:
                await manda('Jungle!')
            elif n == 2:
                await manda('Mid!')
            elif n == 3:
                await manda('Adc!')
            elif n == 4:
                await manda('Sup!')
        
        elif comando == 'roleta' and argumentos == "game":
            n = random.randrange(0, len(games))
            await manda(games[n]+'!')

        elif comando == 'games' and argumentos == '':
            listaGames = ''
            for i in games:
                listaGames = listaGames + i
                listaGames = listaGames + ", "
            await manda(listaGames[:-2])
            
    if message.content in response_object:
        await manda(response_object[message.content])

    if ';-;' in message.content:
        await manda(';-;')
    
    if f'pepemonkas' in message.content:
        await manda(f'{pepemonkas}')

client.run(btoken)

