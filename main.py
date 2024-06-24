import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command(name="convert")
async def convert(ctx, value: float, from_unit: str, to_unit: str):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    result = None

    if from_unit == "kg" and to_unit == "lbs":
        result = value * 2.20462
        await ctx.send(f'{value} kg is {result:.2f} lbs')
    elif from_unit == "lbs" and to_unit == "kg":
        result = value / 2.20462
        await ctx.send(f'{value} lbs is {result:.2f} kg')
    elif from_unit == "inch" and to_unit == "cm":
        result = value * 2.54
        await ctx.send(f'{value} inch is {result:.2f} cm')
    elif from_unit == "cm" and to_unit == "inch":
        result = value / 2.54
        await ctx.send(f'{value} cm is {result:.2f} inch')
    elif from_unit == "f" and to_unit == "c":
        result = (value - 32) * 5.0/9.0
        await ctx.send(f'{value}°F is {result:.2f}°C')
    elif from_unit == "c" and to_unit == "f":
        result = (value * 9.0/5.0) + 32
        await ctx.send(f'{value}°C is {result:.2f}°F')
    else:
        await ctx.send("Invalid conversion units. Please use 'kg' to 'lbs', 'lbs' to 'kg', 'inch' to 'cm', 'cm' to 'inch', 'f' to 'c', or 'c' to 'f'.")

bot.run(TOKEN)