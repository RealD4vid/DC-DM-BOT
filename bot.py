import discord
from discord.ext import commands

TOKEN = "MTMzODU1MzIwMzYyODgzNDg2Ng.GC5fNP.XP8a-myHWnarRMbJNK364SbtGda6EA734jc5RE"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Přihlášen jako {bot.user}')

@bot.command()
async def dm(ctx, user: discord.User, *, message):
    try:
        await user.send(message)
        await ctx.send(f'✅ Zpráva poslána uživateli {user.name}!')
    except:
        await ctx.send('❌ Nelze poslat DM zprávu.')

bot.run(TOKEN)
