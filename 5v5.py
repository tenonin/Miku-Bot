import discord
import asyncio
import random
from discord.ext import commands
from discord.utils import get
import json

with open('C:/Users/Pichau/Desktop/faculdade/Machine learning/Projetos/config.json') as json_data_file:
    data = json.load(json_data_file)

champions = {'aatrox':['Jax','Renekton','Teemo','Riven']}

# Store config details
token = data['token']
prefix = data['prefix']
key = data['key']
modules = data['modules']

bot = commands.Bot(command_prefix=prefix)

intents = discord.Intents.all()
client = discord.Client(intents=intents)

ferro = []
bronze = []
prata = []
ouro = []
platina = []
diamante = []

@client.event
async def on_ready():
    print("5v5 LIGADO")
    print("----------------BOT WORKING----------------")

@client.event
async def on_message(message,*args):
    if message.content.lower() == prefix + "5v5":
        
        channel = message.channel

        lista = []
        vermelho = []
        azul = []
        dict = {0:[],1:[],2:[],3:[],4:[],5:[]}

        guild_id = message.guild.id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        cargo_ferro = discord.utils.get(guild.roles,name="Ferro")
        cargo_bronze = discord.utils.get(guild.roles,name="Bronze")
        cargo_prata = discord.utils.get(guild.roles,name="Prata")
        cargo_ouro = discord.utils.get(guild.roles,name="Ouro")
        cargo_platina = discord.utils.get(guild.roles,name="Platina")
        cargo_diamante = discord.utils.get(guild.roles,name="Diamante")

        lista_cargos = [cargo_bronze,cargo_diamante,cargo_ferro,cargo_ouro,cargo_platina,cargo_prata]

        await message.add_reaction('😎')
        await asyncio.sleep(45)
        message = await message.channel.fetch_message(message.id)
        
        positive = 0
        for reaction in message.reactions:
            if reaction.emoji == '😎':
                positive = reaction.count - 1
                
            async for user in reaction.users():
                lista.append(user)


            lista.pop(0)

            for i in lista_cargos:
                for j in lista:
                    if i in j.roles:
                        if i == cargo_ferro and j != 'Miku Bot':
                            dict[0].append(j.name)
                        elif i == cargo_bronze:
                            dict[1].append(j.name)
                        elif i == cargo_prata:
                            dict[2].append(j.name)
                        elif i == cargo_ouro:
                            dict[3].append(j.name)
                        elif i == cargo_platina:
                            dict[4].append(j.name)
                        elif i == cargo_diamante and j != 'Tundierri':
                            dict[5].append(j.name)
                        else:
                            dict[2].append(j.name)
                
            print(dict)

            for i in dict:
                random.shuffle(dict[i])

            flag = 0
            for i in dict:
                for j in dict[i]:
                    if flag == 0:
                        azul.append(j)
                        flag = 1
                    else:
                        flag = 0
                        vermelho.append(j)

            print(azul, vermelho)

            if positive < 10:
                await channel.send('Precisam de mais {0} pessoas para fazer o Xinco xis Xinco'.format(10-positive))
                

            else:
                embed = discord.Embed(
                    description = 'Time azul:\n{0}\n{1}\n{2}\n{3}\n{4}\n-----------x-----------\nTime Vermelho:\n{5}\n{6}\n{7}\n{8}\n{9}\n'.format(azul[0],azul[1],azul[2],azul[3],azul[4],vermelho[0],vermelho[1],vermelho[2],vermelho[3],vermelho[4],)
                    )
                embed.set_author(name = '5v5', icon_url = 'https://i.imgur.com/kJ0zem8.jpg')
                embed.set_thumbnail(url = 'https://i.imgur.com/9t1rAP0.jpg')
            
                await channel.send(embed = embed)
                

    if message.content.lower() == prefix + 'elo':
        
        channel = message.channel

        guild_id = message.guild.id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        
        cargo_ferro = discord.utils.get(guild.roles,name="Ferro")
        cargo_bronze = discord.utils.get(guild.roles,name="Bronze")
        cargo_prata = discord.utils.get(guild.roles,name="Prata")
        cargo_ouro = discord.utils.get(guild.roles,name="Ouro")
        cargo_platina = discord.utils.get(guild.roles,name="Platina")
        cargo_diamante = discord.utils.get(guild.roles,name="Diamante")

        print(cargo_bronze == None)
        
        if cargo_ferro == None:
            await guild.create_role(name='Ferro',colour=discord.Colour(0x607D8B))
        if cargo_bronze == None:
            await guild.create_role(name='Bronze',colour = discord.Colour(0xEB403B))
        if cargo_prata == None:
            await guild.create_role(name='Prata',colour=discord.Colour(0xAAB9CD))
        if cargo_ouro == None:
            await guild.create_role(name='Ouro',colour= discord.Colour(0xF1C40F))
        if cargo_platina == None:
            await guild.create_role(name='Platina',colour=discord.Colour(0x16A067))
        if cargo_diamante == None:
            await guild.create_role(name='Diamante',colour=discord.Colour(0x3F9FDF))

        embed = discord.Embed(
            title = 'Elo',
            description = 'Escolha seu elo\n0️⃣ - Ferro\n1️⃣ - Bronze\n2️⃣ - Prata\n3️⃣ - Ouro\n4️⃣ - Platina\n5️⃣ - Diamante\n'
        )

        msg = await channel.send(embed = embed)
        await msg.add_reaction('0️⃣')
        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')
        await msg.add_reaction('4️⃣')
        await msg.add_reaction('5️⃣')

    if message.content.lower() == prefix + 'ranking':

        channel = message.channel

        lista_elo = []

        guild_id = message.guild.id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        

        elo_dict = {'Diamante':[],'Platina':[],'Ouro':[],'Prata':[],'Bronze':[],'Ferro':[]}

        cargo_ferro = discord.utils.get(guild.roles,name="Ferro")
        cargo_bronze = discord.utils.get(guild.roles,name="Bronze")
        cargo_prata = discord.utils.get(guild.roles,name="Prata")
        cargo_ouro = discord.utils.get(guild.roles,name="Ouro")
        cargo_platina = discord.utils.get(guild.roles,name="Platina")
        cargo_diamante = discord.utils.get(guild.roles,name="Diamante")

        lista_cargos = [cargo_bronze,cargo_diamante,cargo_ferro,cargo_ouro,cargo_platina,cargo_prata]

        for user in guild.members:
            lista_elo.append(user)

        for i in lista_cargos:
            for j in lista_elo:
                if i in j.roles:
                    if i == cargo_ferro and j.name != 'Miku Bot':
                        elo_dict['Ferro'].append(j.name)
                    if i == cargo_bronze:
                        elo_dict['Bronze'].append(j.name)
                    if i == cargo_prata:
                        elo_dict['Prata'].append(j.name)
                    if i == cargo_ouro:
                        elo_dict['Ouro'].append(j.name)
                    if i == cargo_platina:
                        elo_dict['Platina'].append(j.name)
                    if i == cargo_diamante:
                        elo_dict['Diamante'].append(j.name)

        embed = discord.Embed(
            title = 'Elo do server',
            description = 'Diamante:\n{0}\nPlatina:\n{1}\nOuro:\n{2}\nPrata:\n{3}\nBronze:\n{4}\nFerro:\n{5}'.format(elo_dict['Diamante'],elo_dict['Platina'],elo_dict['Ouro'],elo_dict['Prata'],elo_dict['Bronze'],elo_dict['Ferro'])
        )

        await channel.send(embed = embed)

    if message.content.lower().startswith(prefix + 'opgg'):

        print(message.content)

        args = message.content.split()
        channel = message.channel

        url = 'http://br.op.gg/'

        print(args)

        if len(args) == 2:
            url += 'summoner/userName=' + args[1]
        elif len(args) > 2:
            url += 'multi/query=' + args[1]
            for i in range(2, len(args)):
                url += '%2C' + args[i]

        await channel.send(url)

    if message.content.lower().startswith(prefix + 'matchup'):

        print(message.content)

        args = message.content.split()
        channel = message.channel

        embed = discord.Embed(
            title = 'matchups x '+ args[1],
            description = str(champions[args[1]])
        )


        await channel.send(embed = embed)

@client.event
async def on_raw_reaction_add(payload):

    userId = payload.user_id
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

    author = await guild.fetch_member(userId)
    
    cargo_ferro = discord.utils.get(guild.roles,name="Ferro")
    cargo_bronze = discord.utils.get(guild.roles,name="Bronze")
    cargo_prata = discord.utils.get(guild.roles,name="Prata")
    cargo_ouro = discord.utils.get(guild.roles,name="Ouro")
    cargo_platina = discord.utils.get(guild.roles,name="Platina")
    cargo_diamante = discord.utils.get(guild.roles,name="Diamante")


    lista_cargos = [cargo_bronze,cargo_diamante,cargo_ferro,cargo_ouro,cargo_platina,cargo_prata]

    role = None

    for i in lista_cargos:
        if i in author.roles:
            return
        else:
            if payload.emoji.name == '0️⃣':
                role = discord.utils.get(guild.roles, name = 'Ferro')

            elif payload.emoji.name == '1️⃣':
                role = discord.utils.get(guild.roles, name = 'Bronze')
                
            elif payload.emoji.name == '2️⃣':
                role = discord.utils.get(guild.roles, name = 'Prata')
                
            elif payload.emoji.name == '3️⃣':
                role = discord.utils.get(guild.roles, name = 'Ouro')
                
            elif payload.emoji.name == '4️⃣':
                role = discord.utils.get(guild.roles, name = 'Platina')
                
            elif payload.emoji.name == '5️⃣':
                role = discord.utils.get(guild.roles, name = 'Diamante')
                

    if role is not None:
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

        if member is not None:
            await member.add_roles(role)

client.run("ODI0NzAyOTQ3ODc0MTc3MDU0.YFzOeQ.-kDNFilSs2lPW5VrTO9uxNtRpvI")