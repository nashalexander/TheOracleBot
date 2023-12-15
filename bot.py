import discord
import os
from dotenv import load_dotenv

import discord_message_client as dmc
# import discord_command_bot as dcb

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# TODO: this does not work
# client = dcb.get_discord_bot()

client = dmc.get_discord_client()
client.run(TOKEN)