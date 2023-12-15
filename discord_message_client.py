import discord

import image_generation

def get_discord_client():
    # Configure intents to only read messages
    
    intents = discord.Intents.default()
    intents.guilds = True
    intents.messages = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        print(f'incoming message: {message}')
        if message.author == client.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('world')
        
        if message.content.startswith('/image'):
            result = await image_generation.appendToImageQueue(message.content.split("/image ")[1])
            if result:
                await message.channel.send('image queued')
            else:
                await message.channel.send('image not queued')
    
    return client