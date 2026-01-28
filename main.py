import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.tree.sync()  # sincroniza todos los slash commands
    print(f"Conectado como {bot.user} y slash commands sincronizados")

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,  # También puede ser playing, listening, streaming
            name="Servidor de Gonza MFL"
        )
    )


@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong!")

@bot.tree.command(name="info", description="información del bot")
async def info(interaction: discord.Interaction):
    await interaction.response.send_message("Bot desarollado por Gonza MFL, para su servidor de discord")

@bot.tree.command(name="gmfl", description="Te da el link al canal de Gonza MFL")
async def gmfl(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.youtube.com/channel/UCVD5mR3X6JouRPlDuUfYrkQ")

@bot.tree.command(name="avatar", description="Muestra el avatar de un usuario")
async def avatar(interaction: discord.Interaction, usuario: discord.Member | None = None):

    # Si no se especifica usuario, usa el que ejecutó el comando
    usuario = usuario or interaction.user

    embed = discord.Embed(
        title=f"Avatar de {usuario.name}",
        color=discord.Color.blue()
    )
    embed.set_image(url=usuario.display_avatar.url)

    await interaction.response.send_message(embed=embed)


bot.run(TOKEN)