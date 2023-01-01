import os
import discord
import tomllib
import config
import json

import vitals

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'{bot.user} is up and ready to go!')

def load_cogs():
    for file in os.listdir(config.COGS):
        if file.endswith('.py'):
            bot.load_extension(config.COGS.replace('/', '.') + file[:-3])

    print(f'\n{"ALL COGS LOADED":=^50}')

@bot.slash_command()
async def register(ctx: discord.ApplicationContext):
    if vitals.is_registered(ctx.user.id):
        await ctx.respond('You are already registered!', ephemeral=True)
        return

    with open(config.USER_FILES + 'users.json', 'r') as f:
        text = json.load(f)
    text[str(ctx.user.id)] = {'color': 0}
    with open(config.USER_FILES + 'users.json', 'w') as f:
        json.dump(text, f, indent=4)

    await ctx.respond('You have been registered!')

def main():
    load_cogs()
    bot.run(config.TOKEN)

if __name__ == '__main__':
    main()
