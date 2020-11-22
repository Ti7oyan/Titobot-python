import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">")


# Events


@bot.event  # Displays "'X' Twitch channel" has game activity
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="", url=""))
    print('Bot is ready')


# Text commands


@bot.command()  # Say "Hello!" after >hello
async def hello(ctx):
    await ctx.send('Hello!')


@bot.command(aliases=['s'])  # Make a sum between two numbers
async def sum(ctx, one: int, two: int):
    await ctx.send(one + two)


@bot.command(aliases=['r'])  # Make a subtraction between two numbers
async def subst(ctx, one: int, two: int):
    await ctx.send(one - two)


@bot.command(aliases=["x"])  # Make a multiplication between two numbers
async def multip(ctx, one: int, two: int):
    await ctx.send(one * two)


@bot.command(aliases=["d"])  # Make a division between two numbers
async def divi(ctx, one: int, two: int):
    await ctx.send(one // two)


# Moderation commands (kick, ban, mute)


@bot.command(aliases=["k"])  # Kick a member using >kick @mention + reason
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=" Reason not provided"):
    await member.send("You were been kicked because " + reason)
    await member.kick(reason=reason)


@bot.command(aliases=['b'])  # Ban a member using >ban @mention + reason
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=" Reason not provided"):
    await member.send('You were been banned because ' + reason)
    await member.ban(reason=reason)


@bot.command(aliases=["ub"])  # Unban a member using >unban user_name#discrimination
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator) == (member_name, member_disc):

            await ctx.guild.unban(user)
            await ctx.send(member_name + " was unbanned.")


@bot.command(aliases=['m'])  # Mute a member using >mute @mention
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role()

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " is now muted.")

# Create a role named "Muted", type "\@Muted" and copy and paste the ID on the ctx.guild.get_role place


@bot.command(aliases=['um'])  # Unmute a member using >unmute @mention
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role()

    await member.remove_roles(muted_role)

    await ctx.send(member.mention + " is no longer muted.")

# Create a role named "Muted", type "\@Muted" and copy and paste the ID on the ctx.guild.get_role place


# Extras (-)

# Info commands (-)

bot.run('')

# Thanks to: Code With Swastik, Fazt, AcademiaCoder and all of the other Python users.
# Code by: Ti7oyan
