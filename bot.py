import discord
from discord.ext import commands
import logging
import random
from dotenv import load_dotenv
import os
import aiohttp
import youtube_dl
import asyncio

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
intents.message_content = True  #Necesario para recibir el contenido de los mensajes
intents.members = True #Necesario para detectar cuando un miembro se une
logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} ha iniciado sesión.')

@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola! ¿Cómo estás?')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f'¡Bienvenido al servidor, {member.mention}! Love it. ❤️')

@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f'{member.mention} ha dejado el servidor. Que triste.')

@bot.command()
async def helpB(ctx):
    embed = discord.Embed(
        title="Lista de comandos",
        description="Aquí tienes los comandos disponibles para usar con este bot:",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="`!hola`",
        value="El bot te saluda.",
        inline=False
    )
    embed.add_field(
        name="`!deoder [@usuario]`",
        value="Declara tu amor a alguien o a ti mismo si no mencionas a nadie.",
        inline=False
    )
    embed.add_field(
        name="`!kissB [@usuario1] [@usuario2]`",
        value="Besa a alguien del servidor (atrevido).",
        inline=False
    )
    embed.add_field(
        name="`!palo [@usuario]`",
        value="Muestrale tu cariño a alguien con un palo.",
        inline=False
    )
    embed.add_field(
        name="`!gaymeter`",
        value="Mira que tan gay eres hoy.",
        inline=False
    )
    embed.add_field(
        name="`!brianlove`",
        value="Cuenta una historia de amor.",
        inline=False
    )
    embed.add_field(
        name="`!help`",
        value="Muestra esta lista de comandos.",
        inline=False
    )
    embed.set_footer(text="¡Espero que disfrutes usando el bot! Y perdoname Samuel JAJJAJAJA")
    await ctx.send(embed=embed)

@bot.command()
async def kissB(ctx, member1: discord.Member, member2: discord.Member):
    gifs = [
        "https://media.giphy.com/media/bGm9FuBCGg4SY/giphy.gif",
        "https://media.giphy.com/media/hnNyVPIXgLdle/giphy.gif",
        "https://i.pinimg.com/originals/d6/a7/74/d6a77447dcde409dd8bff80a9cb3ee28.gif",
        "https://i.gifer.com/Jr4.gif"
    ]
    gif = random.choice(gifs)

    embed = discord.Embed(
        title="💋 ¡Un beso ha ocurrido!",
        description=f"{member1.mention} y {member2.mention} se han dado un beso.",
        color=discord.Color.pink()
    )
    embed.set_image(url=gif)
    await ctx.send(embed=embed)

@bot.command()
async def palo(ctx, user: discord.Member):
    gif = "https://c.tenor.com/_x5kGlaLOwYAAAAd/tenor.gif"

    embed = discord.Embed(
        title="¡Palo por ese culo!",
        description=f"{ctx.author.mention} le ha metido un palo a {user.mention} 💀.",
        color=discord.Color.orange()
    )
    embed.set_image(url=gif)
    await ctx.send(embed=embed)

"""@bot.command()
async def chiste(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://v2.jokeapi.dev/joke/Miscellaneous,Dark?lang=es") as response:
            if response.status == 200:
                data = await response.json()
                if not data.get("error"):
                    #Verificamos el tipo de chiste
                    if data["type"] == "single":
                        joke = data["joke"]
                        await ctx.send(f"Aquí tienes un chiste! {joke}")
                    elif data["type"] == "twopart":
                        setup = data["setup"]
                        delivery = data["delivery"]
                        await ctx.send(f"Aquí tienes un chiste! {setup} - {delivery}")
                else:
                    await ctx.send("No pude obtener un chiste en este momento. Inténtalo más tarde.")
            else:
                await ctx.send("Error conectandome a la API para obtener un chiste. Inténtalo más tarde.")"""

@bot.command()
async def gaymeter(ctx):
    porcentaje = random.randint(0, 100)
    embed = discord.Embed(
        title="🌈 Gaymeter",
        description=f"{ctx.author.mention} se siente un **{porcentaje}% gay**. Love it!",
        color=discord.Color.magenta()
    )
    await ctx.send(embed=embed)

@bot.command()
async def brianlove(ctx):
    gif = "https://i.pinimg.com/originals/ae/0a/e5/ae0ae547e909d3dbd89d94fb2a0d72e8.gif"
    historia = (
        "Todo comenzó cuando Fots, en una llamada, le confesó a Brian lo que sentía.\n\n"
        "Con una sonrisa nerviosa, Fots dijo: **'Te amo, Brian'**. "
        "Y entonces, Brian respondió con su característico acento gringo:\n\n"
        "**'Love you too.'** ❤️"
    )
    embed = discord.Embed(
        title="💖 La historia de amor entre Brian y Fots",
        description=historia,
        color=discord.Color.red()
    )
    embed.set_image(url=gif)
    embed.set_footer(text="El amor siempre gana. Love it.")
    await ctx.send(embed=embed)

@bot.command()
async def deoder(ctx, user: discord.Member = None):  #Usuario opcional
    gif = "https://media.tenor.com/lgjHt3_kqo8AAAAM/blushing-gif-blush-emoji.gif"
    
    #Si no se menciona a nadie, se usa el autor del mensaje
    if user is None:
        user = ctx.author
    
    embed = discord.Embed(
        title="Deoder",
        description=f"Yo te amo, {user.mention}!",
        color=discord.Color.orange()
    )
    embed.set_image(url=gif)
    embed.set_footer(text="¡Que viva el amor!")
    await ctx.send(embed=embed)

"""@bot.command()
async def surprise(ctx):
    await ctx.send("¡Sorpresa! Que pendejo 🎵\nhttps://youtu.be/dQw4w9WgXcQ")"""

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Parece que olvidaste mencionar a algún friki del grupo. Por favor, revisa el comando e inténtalo de nuevo.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("No encontré a ese friki que mencionas. Asegúrate de mencionarlo correctamente.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Ese comando no existe. Usa `!help` para ver los comandos disponibles.")
    else:
        logging.error(f"Error inesperado en el comando {ctx.command}: {error}")
        await ctx.send("Ha ocurrido un error inesperado. Inténtalo de nuevo más tarde.")

bot.run(token)