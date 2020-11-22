import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")
client.remove_command('help')


# Events


@client.event  # Displays "X Twitch channel" has game activity
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="YOUR_CHANNEL", url="YOUR_URL"))
    print('Bot is ready')


@client.event  # Simple error message
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to do that")
        await ctx.message.delete()
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


@client.command(aliases=["d"])  # Make a division between two numbers
async def divid(ctx, one: int, two: int):
    await ctx.send(one // two)


# Clear


@client.command()  # Clear X messages of a channel with >clear
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


# Reactions
# Attention: This section has spanish phrases

# Hug

@client.command(pass_context=True, aliases=['h1'])  # Displays a embed with the names of the author, the mentioned user
# and a gif. There are five variants (hug1, hug2, hug3, etc.)
async def hug1(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} abraza a {member.name}', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/r9aU2xv.gif")

    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['h2'])
async def hug2(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} abraza con mucho amor a {member.name}', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/wOmoeF8.gif")

    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['h3'])
async def hug3(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} abraza apasionadamente a {member.name}', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/v47M1S4.gif")

    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['h4'])
async def hug4(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} abraza con cariño a {member.name}', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/4oLIrwj.gif")

    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['h5'])
async def hug5(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} tranquiliza a {member.name} con un abrazo',
                          color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/ntqYLGl.gif")

    await ctx.send(embed=embed)


# Kiss


@client.command(pass_context=True, aliases=['k1'])  # Displays a embed with the names of the author, the mentioned user
# and a gif. There are five variants (kiss1, kiss2, kiss3, etc.)
async def kiss1(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} besa a {member.name} <3', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/II1bakc.gif")

    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['k2'])
async def kiss2(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} besa con cariño a {member.name}', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/MzAjNdv.gif")

    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['k3'])
async def kiss3(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} le roba un beso a {member.name}', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/FozOXkB.gif")

    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['k4'])
async def kiss4(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} besa apasionadamente a {member.name} UwU',
                          color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/I159BUo.gif")

    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['k5'])
async def kiss5(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} besa por sorpresa a {member.name}', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/TDVZwUB.gif")

    await ctx.send(embed=embed)


# Pat

@client.command(pass_context=True, aliases=['p1'])  # Displays a embed with the names of the author, the mentioned user
# and a gif. There are five variants (pat1, pat2, pat3, etc.)
async def pat1(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} acaricia a {member.name}', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/UWbKpx8.gif")

    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['p2'])
async def pat2(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} le hace cariñitos a {member.name}', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/2k0MFIr.gif")

    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['p3'])
async def pat3(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} le hace mimitos a {member.name}', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/LUypjw3.gif")

    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['p4'])
async def pat4(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} le hace caricias a {member.name}', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/2lacG7l.gif")

    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['p5'])
async def pat5(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} acaricia la cabeza de {member.name}', color=discord.Color.red())
    embed.set_image(url="https://i.imgur.com/4ssddEQ.gif")

    await ctx.send(embed=embed)


# Moderation commands (kick, ban, mute)


@client.command(aliases=["k"])  # Kick a member using >kick @mention + reason
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=" Reason not provided"):
    await member.send("You were been kicked because: " + reason)
    await member.kick(reason=reason)
    await ctx.send(f"{member} was kicked for " + reason)


@client.command(aliases=['b'])  # Ban a member using >ban @mention + reason
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=" Reason not provided"):
    await member.send('You were been banned because: ' + reason)
    await member.ban(reason=reason)
    await ctx.send(f"{member} was banned for " + reason)


@client.command(aliases=["ub"])  # Unban a member using >unban user_name#discrimination
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name + " was unbanned.")


@client.command(aliases=['m'])  # Mute a member using >mute @mention
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role()

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " is now silenced.")

# Create a role named "Muted", type "\@Muted" and copy and paste the ID on the 'ctx.guild.get_role()' place


@client.command(aliases=['um'])  # Unmute a member using >unmute @mention
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role()

    await member.remove_roles(muted_role)

    await ctx.send(member.mention + " is no longer silenced.")

# Create a role named "Muted", type "\@Muted" and copy and paste the ID on the 'ctx.guild.get_role()' place


# Help commands


@client.command()  # Displays "help" embed
async def help(ctx):
    em = discord.Embed(color=discord.Color.red())
    em.set_author(name="Help")
    em.add_field(name="Moderation", value=">helpmod", inline=False)
    em.add_field(name="Calc", value=">helpcalc", inline=False)
    em.add_field(name="Reactions", value=">helpreact", inline=False)
    await ctx.send(embed=em)


@client.command()  # Displays "helpmod" embed
async def helpmod(ctx):
    em = discord.Embed(color=discord.Color.red())
    em.set_author(name="Moderation")
    em.add_field(name='Kick', value='>kick @user [reason]', inline=False)
    em.add_field(name='Ban', value='>ban @user [reason]', inline=False)
    em.add_field(name='Unban', value='>unban user#XXXX', inline=False)
    em.add_field(name='Mute', value='>mute @user', inline=False)
    em.add_field(name='Unmute', value='>unmute @user', inline=False)
    await ctx.send(embed=em)


@client.command()  # Displays "helpcalc" embed
async def helpcalc(ctx):
    em = discord.Embed(color=discord.Color.red())
    em.set_author(name="Calc")
    em.add_field(name='Sum', value='>sum [num1] [num2]', inline=False)
    em.add_field(name='Subtract', value='>subt [num1] [num2]', inline=False)
    em.add_field(name='Multiplication', value='>multip [num1] [num2]', inline=False)
    em.add_field(name='Division', value='>divid [num1] [num2]', inline=False)
    await ctx.send(embed=em)


@client.command()  # Displays "helpreact" embed
async def helpreact(ctx):
    em = discord.Embed(color=discord.Color.red())
    em.set_author(name="Reactions")
    em.add_field(name='Hug', value='>hug(1-5) @user or >h(1-5) @user', inline=False)
    em.add_field(name='Kiss', value='>kiss(1-5) @user or >k(1-5) @user', inline=False)
    em.add_field(name='Pat', value='>pat(1-5) @user or >p(1-5) @user', inline=False)
    await ctx.send(embed=em)


# Token

client.run('YOUR_TOKE_HERE')

# Thanks to: Code With Swastik, Fazt, AcademiaCoder and all of the other Python users.
# Code by: Ti7oyan
# Titobot 2020
