import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType


client = commands.Bot(command_prefix='a!', intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.do_not_disturb,
        activity=discord.Game(f"On {len(client.guilds)} servers | a!help"))
    print('online!')
    DiscordComponents(client)


@client.command()
async def emojify(ctx, *, text):
    emojis = []
    for s in text:
        if s.isdecimal():
            num2emo = {
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine'
            }

            emojis.append(f':{num2emo.get(s)}:')
        elif s.isalpha():
            emojis.append(f':regional_indicator_{s}: ')
        else:
            emojis.append(s)

    await ctx.send(''.join(emojis))

client.run(' [ Paste Your Bot Token Here ] ')