import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

class PPBot(commands.Bot):
    def __init__(self, *args):
        super().__init__(command_prefix=args[0], description=args[1], intents=intents)

bot = PPBot(">", "Bot for Programmers Palace", intents=intents)

ppLogo = "https://cdn.discordapp.com/avatars/823751670210363393/472d53a711b5fe4393b6bc5dc9f6e47a.webp?size=2048"

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="with code"))
    print("Programers Palace Bot is ready")

@bot.event
async def on_member_join(member):
  channel = await bot.fetch_channel(823960806260604928)
  embed = discord.Embed(title=f"{member.name} Joined!", description=f"{member.name}.exe has been sucessfully downloaded!", colour= discord.colour.Color.blue())
  embed.set_author(name="Programers Princess", icon_url=ppLogo)
  embed.set_thumbnail(url=member.avatar_url)
  await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
  channel = await bot.fetch_channel(823960806260604928)
  embed = discord.Embed(title= f"{member.name} Left!", description= f"{member.name}.exe has stopped working.", colour= discord.colour.Color.blue())
  embed.set_author(name= "Programers Princess", icon_url= ppLogo)
  embed.set_thumbnail(url= member.avatar_url)
  await channel.send(embed= embed)


@bot.command()
async def ja(ctx):
    await ctx.send("https://media.discordapp.net/attachments/767475855990456363/823756179812646922/unknown.png")

@bot.command()
async def gi(ctx):
    await ctx.send("https://media.discordapp.net/attachments/267131764827357184/823690855864991744/unknown.png")

@bot.command()
async def invite(ctx):
    await ctx.send("https://discord.gg/jP4urjM")

@bot.command()
async def report(ctx, *, message):
    mod = await client.fetch_user(756757056941326397)

    embed = discord.Embed(title= "New Report", description= report, colour= discord.colour.Color.red())
    embed.set_author(name= ctx.author.name, icon_url= ctx.author.avatar_url)

    embed1 = discord.Embed(title= "Report Submitted!", description= report, colour= discord.colour.Color.green())
    embed1.set_author(name= ctx.author.name, icon_url= ctx.author.avatar_url)

    await mod.send(embed=embed)
    await ctx.send(embed=embed1)

@bot.group(pass_context=True)
async def nick(ctx, user: discord.Member, name: str = None):
    if name is None:
        return await ctx.send("Please specify a nickname, or 'clear' to remove your current nickname.")
    elif name == "clear":
        pass
    else:
        try:
            await user.edit(nick=name)
        except discord.Forbidden:
            embed = discord.Embed(title="Error", description= "I don't have permission to change your nickname!", colour= discord.colour.Color.red())
            embed.set_author(name= "Programers Princess", icon_url= ppLogo)
            await ctx.send(embed= embed, delete_after=3)

@nick.command()
async def clear(ctx, user):
    await user.edit(nick="")
    embed = discord.Embed(title="Nickname Changed!", description= f"Your nickname has been changed to {nickname}!", colour= discord.colour.Color.green())
    embed.set_author(name= "Programers Princess", icon_url= ppLogo)
    await channel.send(embed= embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason):
    try:
        import re

        await member.kick(reason=reason)

        embed = discord.Embed(title= "User Kicked", description= f"{target.name}.exe has been moved to the recycle bin", colour= discord.colour.Colour.green())
        embed.set_author(name= "Programers Princess", icon_url= ppLogo)
        embed.set_thumbnail(url= target.avatar_url)
        await ctx.send(embed= embed)
    except discord.Forbidden:
        embed= discord.Embed(title= "Error", description= "I don't have permission to kick this person", colour= discord.colour.Color.red())
        await ctx.send(embed= embed) 

client.run("Token")