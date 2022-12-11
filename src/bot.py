import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

from src import responses
from src import log

logger = log.setup_logger()

load_dotenv()


async def send_message(message, sku, size_us):
    await message.response.defer()
    try:
        r = await responses.handle_response(sku, size_us)
        if r:
            await message.followup.send(r)
        else:
            await message.followup.send("No results 🤷‍♂️")

    except Exception as e:
        await message.followup.send("Contact your administrator 🐛")
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    activity = discord.Activity(type=discord.ActivityType.watching, name="Monitor +10 shops 👟")
    client = commands.Bot(command_prefix='!', intents=intents, activity=activity)

    @client.event
    async def on_ready():
        await client.tree.sync()
        logger.info(f'{client.user} is now running!')

    @client.tree.command(name="payout", description="Get the best reselling price of sneakers")
    async def payout(interaction: discord.Interaction, *, sku: str, size_us: str):
        if interaction.user == client.user:
            return

        user_message = sku

        logger.info(f"{str(interaction.user)} → sku '{user_message}' ({str(interaction.channel)})")

        await send_message(interaction, user_message, size_us)

    client.run(os.getenv('TOKEN'))
