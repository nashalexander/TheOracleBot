import discord
import discord.ext

import image_generation

def get_discord_bot():
    bot = commands.Bot()

    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')

    @bot.command(guild_ids=['...'])
    async def hello(ctx):
        await ctx.respond("Hello!")
    
    @bot.command(guild_ids=['...'])
    async def image(ctx, *, arg):
        result = await image_generation.appendToImageQueue(arg)
        if result:
            await ctx.send('image queued')
        else:
            await ctx.send('image not queued')
    
    return bot