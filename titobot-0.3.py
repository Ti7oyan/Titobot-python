import discord
import random
import time
from random import randint

from discord import Embed
from discord.ext import commands


client = commands.Bot(command_prefix="t!")
client.remove_command('help')

# Events


@client.event  # Displays "X Twitch channel" has game activity
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="YOUR_CHANNEL", url="YOUR_CHANNEL_URL"))
    print('Bot is ready')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to do that.")
        time.sleep(0.1)
        await ctx.channel.purge(limit=1)
    else:
        raise error


# Text commands

# Calc

@client.command(aliases=['s'])  # Make a sum between two numbers
async def sum(ctx, one: int, two: int):
    await ctx.send(one + two)


@client.command(aliases=['r'])  # Make a subtraction between two numbers
async def subt(ctx, one: int, two: int):
    await ctx.send(one - two)


@client.command(aliases=["x"])  # Make a multiplication between two numbers
async def multip(ctx, one: int, two: int):
    await ctx.send(one * two)


@client.command(aliases=["d"])  # Make an entire division between two numbers
async def divid(ctx, one: int, two: int):
    await ctx.send(one // two)

# Clear


@client.command(aliases=["clean"])  # Clean X messages in the current channel
async def purge(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{amount} deleted messages.")
    time.sleep(0.1)
    await ctx.channel.purge(limit=1)


# Reactions

# Hug

@client.command(name="hug")  # Displays an "hug" gif, mentioning another user.
async def hug(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} hugs {member.display_name}', color=discord.Color.red())

    listgifs = [
        'https://media.giphy.com/media/DjczAlIcyK1Co/giphy.gif',
        'https://i.imgur.com/IAxUnda.gif',
        'https://i.imgur.com/wOmoeF8.gif',
        'https://media1.tenor.com/images/969f0f462e4b7350da543f0231ba94cb/tenor.gif?itemid=14246498',
        'https://media1.tenor.com/images/5845f40e535e00e753c7931dd77e4896/tenor.gif?itemid=9920978',
        'https://media1.tenor.com/images/1d94b18b89f600cbb420cce85558b493/tenor.gif?itemid=15942846',
        'https://media1.tenor.com/images/94989f6312726739893d41231942bb1b/tenor.gif?itemid=14106856',
        'https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587',
        'https://media1.tenor.com/images/b62f047f8ed11b832cb6c0d8ec30687b/tenor.gif?itemid=12668480',
        'https://media1.tenor.com/images/d3dca2dec335e5707e668b2f9813fde5/tenor.gif?itemid=12668677',
        'https://media1.tenor.com/images/efdd8f53689b1bb3437054d608156e95/tenor.gif?itemid=4986736',
        'https://media1.tenor.com/images/45b1dd9eaace572a65a305807cfaec9f/tenor.gif?itemid=6238016',
        'https://media1.tenor.com/images/b7487d45af7950bfb3f7027c93aa49b1/tenor.gif?itemid=9882931',
        'https://media1.tenor.com/images/e9d7da26f8b2adbb8aa99cfd48c58c3e/tenor.gif?itemid=14721541',
        'https://media1.tenor.com/images/94c44a9898927f22dff399c2c248f433/tenor.gif?itemid=11247364',
        'https://media1.tenor.com/images/f855a0348c55a6d0469f34135510bcb2/tenor.gif?itemid=5690234'

    ]
    response = random.choice(listgifs)
    embed.set_image(url=f"{response}")
    await ctx.send(embed=embed)


# Kiss


@client.command(name="kiss")  # Displays a "kiss" gif, mentioning another user.
async def kiss(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} kisses {member.display_name} <3', color=discord.Color.red())

    listgifs = [
        'https://media.giphy.com/media/jR22gdcPiOLaE/giphy.gif',
        'https://media.giphy.com/media/hnNyVPIXgLdle/giphy.gif',
        'https://media.giphy.com/media/zkppEMFvRX5FC/giphy.gif',
        'https://media.giphy.com/media/vUrwEOLtBUnJe/giphy.gif',
        'https://media.giphy.com/media/G3va31oEEnIkM/giphy.gif',
        'https://media.giphy.com/media/1wmtU5YhqqDKg/giphy.gif',
        'https://media.giphy.com/media/Gj8bn4pgTocog/giphy.gif',
        'https://media.giphy.com/media/kdLyU5mq9mGfm/giphy.gif',
        'https://media.giphy.com/media/oZNdL0smZoHoQ/giphy.gif',
        'https://media.giphy.com/media/rU7RhIQuwGWOc/giphy.gif',
        'https://media.giphy.com/media/nyGFcsP0kAobm/giphy.gif',
        'https://media1.tenor.com/images/b8d0152fbe9ecc061f9ad7ff74533396/tenor.gif?itemid=5372258',
        'https://media1.tenor.com/images/d0cd64030f383d56e7edc54a484d4b8d/tenor.gif?itemid=17382422',
        'https://media1.tenor.com/images/6f455ef36a0eb011a60fad110a44ce68/tenor.gif?itemid=13658106',
        'https://media1.tenor.com/images/9fac3eab2f619789b88fdf9aa5ca7b8f/tenor.gif?itemid=12925177',
        'https://media1.tenor.com/images/61dba0b61a2647a0663b7bde896c966c/tenor.gif?itemid=5262571'

    ]
    response = random.choice(listgifs)
    embed.set_image(url=f"{response}")
    await ctx.send(embed=embed)


# Pat

@client.command(name="pat")  # Displays a "pat" gif, mentioning another user.
async def pat(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} acaricia a {member.display_name}', color=discord.Color.red())

    listgifs = [
        'https://media.giphy.com/media/L2z7dnOduqEow/giphy.gif',
        'https://media.giphy.com/media/ye7OTQgwmVuVy/giphy.gif',
        'https://media.giphy.com/media/ARSp9T7wwxNcs/giphy-downsized.gif',
        'https://media.giphy.com/media/HxDOijFIr4g3S/giphy.gif',
        'https://media.giphy.com/media/osYdfUptPqV0s/giphy-downsized.gif',
        'https://media.giphy.com/media/109ltuoSQT212w/giphy-downsized.gif',
        'https://media.giphy.com/media/5tmRHwTlHAA9WkVxTU/giphy.gif',
        'https://media.giphy.com/media/PHZ7v9tfQu0o0/giphy.gif',
        'https://media.giphy.com/media/rk0RHK2uUAe2I/giphy.gif',
        'https://media.giphy.com/media/SSPW60F2Uul8OyRvQ0/giphy.gif',
        'https://media.giphy.com/media/EGauSkKQZuXxS/giphy.gif',
        'https://i.imgur.com/UWbKpx8.gif',
        'https://i.imgur.com/2k0MFIr.gif',
        'https://i.imgur.com/LUypjw3.gif',
        'https://i.imgur.com/F3cjr3n.gif',
        'https://i.imgur.com/2lacG7l.gif'

    ]
    response = random.choice(listgifs)
    embed.set_image(url=f"{response}")
    await ctx.send(embed=embed)

# Kill


@client.command(name="kill")  # Displays a "kill" gif, mentioning another user.
async def kill(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} kills {member.display_name} >.<', color=discord.Color.red())

    listgifs = [
        'https://media1.tenor.com/images/bb4b7a7559c709ffa26c5301150e07e4/tenor.gif',
        'https://media1.tenor.com/images/2c945adbbc31699861f411f86ce8058f/tenor.gif',
        'https://media1.tenor.com/images/1cb509f145f1f6db7761592545039b0e/tenor.gif',
        'https://media1.tenor.com/images/414f57a7868beaf3800a93b266f51ba9/tenor.gif',
        'https://media1.tenor.com/images/c3cbe5b795cd40c0b51d02711f6e3978/tenor.gif',
        'https://media1.tenor.com/images/0772e1ee8d5baa79d69b69f52d99f648/tenor.gif',
        'https://media1.tenor.com/images/96be5fd3dc9ac47b412a4d2dd0b84fcf/tenor.gif',
        'https://media1.tenor.com/images/0917e9f68e7d277135a9f885f953888b/tenor.gif',
        'https://media1.tenor.com/images/fff8e3bfc80524fe6cf035acf942012b/tenor.gif',
        'https://media1.tenor.com/images/5ef5b545c8377b12fe7edc8f15216d95/tenor.gif',
        'https://media1.tenor.com/images/3815fe03a57a117ef320e08b5a5cc525/tenor.gif',
        'https://media1.tenor.com/images/c15fa28f6cc9cfb014f5a9f9731b698d/tenor.gif',
        'https://media.tenor.com/images/51cf00e44ba2db021871e0275bbbaf80/tenor.gif',
        'https://media1.tenor.com/images/4a552d8b147303c313d613f5c21f8741/tenor.gif',
        'https://media.tenor.com/images/b18a3b35cde34364e625e7850f8b1174/tenor.gif',
        'https://media.tenor.com/images/3135300717d3b2a149b1c0257b51dfd3/tenor.gif'

    ]
    response = random.choice(listgifs)
    embed.set_image(url=f"{response}")
    await ctx.send(embed=embed)


# Punch


@client.command(name="punch")  # Displays a "punch" gif, mentioning another user.
async def punch(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} punches {member.display_name} >.<', color=discord.Color.red())

    listgifs = [
        'https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/tenor.gif',
        'https://media1.tenor.com/images/79cc6480652032a20f1cb5c446b113ae/tenor.gif',
        'https://media1.tenor.com/images/f03329d8877abfde62b1e056953724f3/tenor.gif',
        'https://media1.tenor.com/images/ee3f2a6939a68df9563a7374f131fd96/tenor.gif',
        'https://media1.tenor.com/images/c621075def6ca41785ef4aaea20cc3a2/tenor.gif',
        'https://media1.tenor.com/images/3c95ca85f89068660becde7a31f0f04d/tenor.gif',
        'https://media1.tenor.com/images/2487a7679b3d7d23cadcd51381635467/tenor.gif',
        'https://media1.tenor.com/images/d7c30e46a937aaade4d7bc20eb09339b/tenor.gif',
        'https://media1.tenor.com/images/855c900190fb6abfabaed7da4da6f73c/tenor.gif',
        'https://media.tenor.com/images/b0be50580758732123cdc86b60aa6f09/tenor.gif',
        'https://media1.tenor.com/images/36430033b3549744ce109929cbd6694e/tenor.gif',
        'https://media1.tenor.com/images/60b8d7a2ca6d419a9fcabfc4eb0bc607/tenor.gif',
        'https://media1.tenor.com/images/1ac0a65e08d401a59bed572250521e8f/tenor.gif',
        'https://media1.tenor.com/images/1125596130202a28802dd2fe20804426/tenor.gif',
        'https://media.tenor.com/images/b561ad7377142adf365fe33f20fa45e8/tenor.gif',
        'https://media1.tenor.com/images/7507863ac12c64033c37a6b8bb1f7a0b/tenor.gif'

    ]
    response = random.choice(listgifs)
    embed.set_image(url=f"{response}")
    await ctx.send(embed=embed)


# Sleep


@client.command()  # Displays a "sleep" gif.
async def sleep(ctx):
    embed = discord.Embed(title=f"{ctx.author.name} se siente con sueño.", color=discord.Color.red())

    listgifs = [
        'https://media1.tenor.com/images/7175fe4b5e789b94b41a793e2fd4db3d/tenor.gif',
        'https://media1.tenor.com/images/1cdece239ec7d0fb33d2976d623f5e77/tenor.gif',
        'https://media.tenor.com/images/ebb3a5dd38c58878ebd588ad28e00560/tenor.gif',
        'https://media1.tenor.com/images/0a35a0cc82d3b613086e0f420a94c2ad/tenor.gif',
        'https://media1.tenor.com/images/536666c6ed48d260e68ae067a5e7129c/tenor.gif',
        'https://media1.tenor.com/images/b0daf8299389bf3fa4260a91690f0e12/tenor.gif',
        'https://media1.tenor.com/images/a7e8e8f9fd0a8784012d8f14b09da4a8/tenor.gif',
        'https://media1.tenor.com/images/62299afcedd465b631f9baa9786bd83b/tenor.gif',
        'https://media1.tenor.com/images/51612fc78b9dae95497aa78997e077bb/tenor.gif',
        'https://media1.tenor.com/images/9650b39d78fd6b91456924ad51f79de2/tenor.gif',
        'https://media1.tenor.com/images/df7ebd0a18d155d1aab5626669df1aad/tenor.gif'
    ]
    response = random.choice(listgifs)
    embed.set_image(url=f"{response}")
    await ctx.send(embed=embed)

# FBI


@client.command()  # Displays a "fbi" gif
async def fbi(ctx):
    embed = discord.Embed(title="The FBI arrived, run!.", color=discord.Color.red())
    embed.set_image(url="https://media1.tenor.com/images/813cbbc9db143c042e38bc9732bc69c3/tenor.gif?itemid=12425962")
    await ctx.send(embed=embed)


# Percentages (THIS PART HAS BEEN COMPLETLY WRITTEN IN SPANISH, CHANGE THE PHRASES TO SOME YOU LIKE)


@client.command()  # Determines percentage of "gay" with 3 variables
async def gay(ctx):
    valor = randint(1, 100)
    if valor >= 50:
        await ctx.send(f"{ctx.author.name} es un {valor}% homosexual y se le dio vuelta la tortilla.")
    elif valor <= 20:
        await ctx.send(f"{ctx.author.name} todavia cree en Dios y es un {valor}% homosexual")
    else:
        await ctx.send(f"{ctx.author.name} es {valor}% homosexual.")


@client.command(aliases=['tl'])  # Determines "tula" length with 3 variables
async def tula(ctx):
    valor = randint(0, 100)
    if valor >= 50:
        await ctx.send(f"{ctx.author.name} esta cometiendo un delito cargandose una tula de {valor}cm.")
    elif valor <= 10:
        await ctx.send(f"{ctx.author.name} tiene mucho frio y se le encogio su tulita de {valor}cm.")
    else:
        await ctx.send(f"{ctx.author.name} tiene una tula de {valor}cm, que buena tula.")


@client.command(aliases=['tld'])  # Determines "tula" length of another member
async def tulade(ctx, member: discord.Member):
    valor = randint(0, 100)
    if valor >= 50:
        await ctx.send(f"La tula de {member.mention} es impresionantemente grande y mide {valor}cm.")
    elif valor <= 10:
        await ctx.send(f'La tula de {member.mention} es tan pequeña que mide {valor}cm.')
    else:
        await ctx.send(f"La tula de {member.mention} mide {valor}cm, tremenda tula.")
    
    
@client.command(aliases=["pl"])  # Determines level of "peronismo"
async def peronismlevel(ctx):
    valor = randint(0, 100)
    if valor >= 90:
        embed = discord.Embed(title=f"El nivel de peronismo de {ctx.author.name} es de {valor}%"
                                    f"y es el nuevo ministro de Peron.", color=discord.Color.red())
        embed.set_image(url="http://www.lalupa24.com/wp-content/uploads/2017/10/1487104873185-1-880x494.jpg")
        await ctx.send(embed=embed)

    elif valor <= 15:
        embed = discord.Embed(title=f"{ctx.author.name} no sigue el peronismo y solo es un {valor}% peronista.",
                              color=discord.Color.red())
        embed.set_image(url="https://i.servimg.com/u/f62/19/64/60/76/peron_10.jpg")
        await ctx.send(embed=embed)

    else:
        embed: Embed = discord.Embed(title=f"{ctx.author.name} es un {valor}% peronista", color=discord.Color.red())
        embed.set_image(url="https://lamula.pe/media/uploads/t/33dc611a4888e86a174ccd5af642c217.jpg")
        await ctx.send(embed=embed)


@client.command(aliases=["pld"])  # Determines level of "peronismo" of another member.
async def peronismlevelde(ctx, member: discord.Member):
    valor = randint(0, 100)
    em = discord.Embed(title=f"El nivel de peronismo de {member.display_name} es de {valor}%",
                       color=discord.Color.red())
    em.set_image(url="https://i.imgur.com/hkU4CHw.png")
    await ctx.send(embed=em)


# Moderation commands (kick, ban, mute)


@client.command(aliases=["k"])  # Kick a member using t!kick @mention + reason
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=" Reason not provided"):
    await member.send("You were been kicked, because: " + reason)
    await member.kick(reason=reason)
    await ctx.send(f"{member} was kicked because: " + reason)


@client.command(aliases=['b'])  # Ban a member using t!ban @mention + reason
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=" Reason not provided"):
    await member.send('You were been banned, because: ' + reason)
    await member.ban(reason=reason)
    await ctx.send(f"{member} was banned because: " + reason)


@client.command(aliases=["ub"])  # Unban a member using t!unban user_name#discrimination
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name + " was unbanned.")


@client.command(aliases=['m'])  # Mute a member using t!mute @mention
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(779848810092167189)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " is muted.")


@client.command(aliases=['um'])  # Unmute a member using t!unmute @mention
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(779848810092167189)

    await member.remove_roles(muted_role)

    await ctx.send(member.mention + " is no more long muted.")


# Help commands


@client.command()
async def help(ctx):
    em = discord.Embed(color=discord.Color.red())
    em.set_author(name="Help")
    em.add_field(name="Moderation", value="t!helpmod", inline=False)
    em.add_field(name="Calc", value="t!helpcalc", inline=False)
    em.add_field(name="Reactions", value="t!helpreact", inline=False)
    em.add_field(name="Fun", value="t!helpfun", inline=False)
    await ctx.send(embed=em)


@client.command()
async def helpmod(ctx):
    em = discord.Embed(color=discord.Color.red())
    em.set_author(name="Moderation")
    em.add_field(name='Kick:', value='>t!kick @user [reason]', inline=False)
    em.add_field(name='Ban:', value='t!ban @user [reason]', inline=False)
    em.add_field(name='Unban:', value='t!unban user#XXXX', inline=False)
    em.add_field(name='Mute:', value='t!mute @user', inline=False)
    em.add_field(name='Unmute:', value='t!unmute @user', inline=False)
    await ctx.send(embed=em)


@client.command()
async def helpcalc(ctx):
    em = discord.Embed(color=discord.Color.red())
    em.set_author(name="Calc")
    em.add_field(name='Sum:', value='t!sum [num1] [num2]', inline=False)
    em.add_field(name='Subt:', value='t!subt [num1] [num2]', inline=False)
    em.add_field(name='Multiplication:', value='t!multip [num1] [num2]', inline=False)
    em.add_field(name='Division:', value='t!divid [num1] [num2]', inline=False)
    await ctx.send(embed=em)


@client.command()
async def helpreact(ctx):
    em = discord.Embed(color=discord.Color.red())
    em.set_author(name="Reactions")
    em.add_field(name='Hug:', value='t!hug @user', inline=False)
    em.add_field(name='Kiss:', value='t!kiss @user', inline=False)
    em.add_field(name='Pat:', value='t!pat @user', inline=False)
    em.add_field(name='Kill:', value='t!kill @user', inline=False)
    em.add_field(name='Punch:', value='t!punch @user', inline=False)
    em.add_field(name='Sleep:', value='t!sleep', inline=False)
    em.add_field(name='FBI:', value='t!fbi', inline=False)
    await ctx.send(embed=em)


@client.command()
async def helpfun(ctx):
    em = discord.Embed(color=discord.Color.red())
    em.set_author(name="Fun")
    em.add_field(name='Gay:', value='t!gay', inline=False)
    em.add_field(name='Tula:', value='t!tula', inline=False)
    em.add_field(name='Tulade:', value='t!tulade @user', inline=False)
    em.add_field(name='Peronismolevel:', value='t!pl', inline=False)
    em.add_field(name='Peronismolevelde:', value='t!pld @user', inline=False)
    await ctx.send(embed=em)


# Extras

# Token

client.run('YOUR_TOKEN_HERE')

# Thanks to: Code With Swastik, Fazt, AcademiaCoder and all of the other Python users.
# Code by: Ti7oyan
# Titobot 2020
