import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def wl_add(ctx, member: discord.Member):
    roomka = discord.utils.get(ctx.guild.channels, id = 1092887040741363722)
    message_id = ctx.message.id
    mentioned_rola = member.roles
    invoker_rola = ctx.author.roles
    invoker_role = [role.name for role in invoker_rola]
    mentioned_role = [role.name for role in mentioned_rola]

    pohovor1 = discord.utils.get(ctx.guild.roles, id = 1093630243689996428)
    pohovor2 = discord.utils.get(ctx.guild.roles, id = 1093630280331432128)
    
    for i in range(len(mentioned_role)):
        if mentioned_role[i] == 'pohovor 1':
            await member.remove_roles(pohovor1)
        if mentioned_role[i] == 'pohovor 2':
            await member.remove_roles(pohovor2)
            
    if 'WLADDER' in invoker_role:    
        rola = discord.utils.get(ctx.guild.roles, id = 1092886263343886398)
        await member.add_roles(rola)
        wladder = ctx.author
        await roomka.send(f'Hráčovi {member.mention} bola udelená rola WHITELISTED od {wladder.mention}')
    else:
        wladder = ctx.author
        await ctx.send(f'[MISSING ROLE] Na použitie príkazu nemáš dostatočné role {wladder.mention}', delete_after = 15)
    await ctx.message.delete()

@bot.command()
async def nemoznost_add(ctx, member: discord.Member, arg = 30):
    roomka = discord.utils.get(ctx.guild.channels, id = 1092887040741363722)
    dni = int(arg)
    sekundy = dni * 86400
    
    if dni == 1:
        stringsranda = 'den'
    else:
        stringsranda = 'dni'
    message_id = ctx.message.id
    invoker_rola = ctx.author.roles
    invoker_role = [role.name for role in invoker_rola]
    if 'WLADDER' in invoker_role:    
        rola = discord.utils.get(ctx.guild.roles, id = 1092885420922118174)
        await member.add_roles(rola)
        wladder = ctx.author
        await roomka.send(f'Hráčovi {member.mention} bola udelená rola NEMOŽOSŤ ROBIŤ WL od {wladder.mention} na {dni} {stringsranda}')
        await ctx.message.delete()
        await asyncio.sleep(sekundy)
        await member.remove_roles(rola)  
    else:
        wladder = ctx.author
        await ctx.send(f'[MISSING ROLE] Na použitie príkazu nemáš dostatočné role {wladder.mention}', delete_after = 15)
        await ctx.message.delete()
    
@bot.command()
async def pohovor_1(ctx, member: discord.Member):
    roomka = discord.utils.get(ctx.guild.channels, id = 1092887040741363722)
    message_id = ctx.message.id
    invoker_rola = ctx.author.roles
    invoker_role = [role.name for role in invoker_rola]
    if 'WLADDER' in invoker_role:    
        rola = discord.utils.get(ctx.guild.roles, id = 1092885459341946940)
        await member.add_roles(rola)
        wladder = ctx.author
        await roomka.send(f'Hráčovi {member.mention} bola udelená rola Pohovor 1 od {wladder.mention}')
    else:
        wladder = ctx.author
        await ctx.send(f'[MISSING ROLE] Na použitie príkazu nemáš dostatočné role {wladder.mention}', delete_after = 15)
    await ctx.message.delete()

@bot.command()
async def pohovor_2(ctx, member: discord.Member):
    roomka = discord.utils.get(ctx.guild.channels, id = 1092887040741363722)
    mentioned_rola = member.roles
    message_id = ctx.message.id
    invoker_rola = ctx.author.roles
    invoker_role = [role.name for role in invoker_rola]
    pohovor1 = discord.utils.get(ctx.guild.roles, id = 1092885459341946940)
    mentioned_role = [role.name for role in mentioned_rola]
    for i in range(len(mentioned_role)):
        if mentioned_role[i] == 'pohovor 1':
            await member.remove_roles(pohovor1)
    if 'WLADDER' in invoker_role:    
        rola = discord.utils.get(ctx.guild.roles, id = 1092885501280788590)
        await member.add_roles(rola)
        wladder = ctx.author
        await roomka.send(f'Hráčovi {member.mention} bola udelená rola Pohovor 2 od {wladder.mention}')
    else:
        wladder = ctx.author
        await ctx.send(f'[MISSING ROLE] Na použitie príkazu nemáš dostatočné role {wladder.mention}', delete_after = 15)
    await ctx.message.delete()
bot.run('YOUR_BOT_TOKEN')
