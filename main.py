import os
import discord
from discord.ext import commands

CHANNEL_ID = os.environ.get('CHANNEL_ID')
BOT_ID = os.environ.get('BOT_ID')

if CHANNEL_ID is None or BOT_ID is None:
    print("Please set the CHANNEL_ID and BOT_ID environment variables.")
    exit(1)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', description='descrip', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await clear_channel()

@bot.event
async def clear_channel():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.purge()
        await channel.send('Cleared! Happy Wordling!')
        print(f'Cleared all messages in channel {CHANNEL_ID}\nThe script will now close.')
    else:
        print(f'Channel with ID {CHANNEL_ID} not found')

    await bot.close()

def main():
    print("")

bot.run(BOT_ID)