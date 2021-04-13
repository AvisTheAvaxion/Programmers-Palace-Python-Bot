import discord
from discord.ext import commands
import time

intents = discord.Intents.default()
intents.members = True

version = "A0.0.2"
ppLogo = "https://cdn.discordapp.com/avatars/823751670210363393/472d53a711b5fe4393b6bc5dc9f6e47a.webp?size=2048"

client = commands.Bot(command_prefix=">", help_command=None,  intents=intents)

@client.event
async def on_ready():
  activity = discord.Game(name=f" with code |>help |{version}")
  await client.change_presence(status=discord.Status.online, activity=activity)
  print("Programmers Princess Bot is ready!")

@client.event
async def on_member_join(member):
  channel = await client.fetch_channel(823960806260604928)
  embed = discord.Embed(title= f"{member.name} Joined!", description= f"{member.name}.exe has been sucessfully downloaded!", colour= discord.colour.Color.blue())
  embed.set_author(name= "Programers Princess", icon_url= ppLogo)
  embed.set_thumbnail(url= member.avatar_url)
  await channel.send(embed= embed)

@client.event
async def on_member_remove(member):
  channel = await client.fetch_channel(823960806260604928)
  embed = discord.Embed(title= f"{member.name} Left!", description= f"{member.name}.exe deleted themselves.", colour= discord.colour.Color.blue())
  embed.set_author(name= "Programers Princess", icon_url= ppLogo)
  embed.set_thumbnail(url= member.avatar_url)
  await channel.send(embed= embed)

@client.command()
async def ping(ctx):
  tic = time.perf_counter()
  latency = client.latency
  msg = await ctx.send(f"pong:{round(latency * 1000)}ms |")
  toc = time.perf_counter()

  await msg.edit(content= f"pong:{round(latency * 1000)}ms | {(toc - tic) * 1000:0.0f}ms")

@client.command()
async def test(ctx):
  a = await ctx.send("hi")
  await a.edit(content="test completed")

@client.command()
async def help(ctx):
  embed = discord.Embed(title= "Help", description= "You asked for help", colour= discord.colour.Color.green())
  embed.set_author(name= "Programers Princess", icon_url= ppLogo)
  embed.add_field(name= ">ja", value= "Displays just ask emoji", inline= False)
  embed.add_field(name= ">g", value= "Displays Google It emoji", inline = False)
  embed.add_field(name= ">invite", value= "Displays a server invite", inline = False)
  embed.add_field(name= ">report [message]", value= "A command to report bugs with the bot", inline = False)
  embed.add_field(name= ">nick [nickname]", value= "Changes your nickname", inline = False)
  embed.add_field(name= ">help", value= "A helpful command", inline= False)
  embed.set_footer(text= "Tip or something here?")
          
  await ctx.send(embed= embed)

@client.command()
async def ja(ctx):
  await ctx.send("https://media.discordapp.net/attachments/767475855990456363/823756179812646922/unknown.png")
  await ctx.message.delete()


@client.command()
async def g(ctx):
  await ctx.send("https://media.discordapp.net/attachments/267131764827357184/823690855864991744/unknown.png")
  await ctx.message.delete()

@client.command()
async def invite(ctx):
  await ctx.send("https://discord.gg/jP4urjM")
  await ctx.message.delete()


@client.command()
async def report(ctx):
  msg = ctx.message.content
  report = msg[8:]
  Doomer = await client.fetch_user(756757056941326397)
  #Doomer is 756757056941326397
  #Avis is 364905148083994626

  doomerEmbed = discord.Embed(title= "New Report", description= report, colour= discord.colour.Color.red())
  doomerEmbed.set_author(name= ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
  await Doomer.send(embed= doomerEmbed)

  channelEmbed = discord.Embed(title= "Report Submitted!", description= report, colour= discord.colour.Color.green())
  channelEmbed.set_author(name= ctx.message.author.name, icon_url= ctx.message.author.avatar_url)
  await ctx.send(embed= channelEmbed)

@client.command()
async def nick(ctx):
  try:
    msg = ctx.message.content
    nickname = msg[6:]
    user = ctx.message.author
    await user.edit(nick= nickname)
    
    if ctx.message.content == ">nick clear":
      await user.edit(nick= None)
      embed = discord.Embed(title="Nickname Cleared!", description= "Your nickname has been cleared!", colour= discord.colour.Color.green())
      embed.set_author(name= "Programmers Princess", icon_url= ppLogo)
      msg = await ctx.send(embed= embed)
      await msg.delete(delay= 3)

    
    else:
      embed = discord.Embed(title="Nickname Changed!", description= f"Your nickname has been changed to {nickname}!", colour= discord.colour.Color.green())
      embed.set_author(name= "Programers Princess", icon_url= ppLogo)
      msg = await ctx.channel.send(embed= embed)
      # await msg.delete(delay= 3)

  except discord.Forbidden:
    embed = discord.Embed(title="Error", description= "I don't have permission to change your nickname!", colour= discord.colour.Color.red())
    embed.set_author(name= "Programers Princess", icon_url= ppLogo)
    msg = await ctx.channel.send(embed= embed)



















@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx):
  msg = ctx.message.content
  try:
    target = ctx.message.mentions[0]
    
  except IndexError:
    embed= discord.Embed(title= "Error", description= "No member mentioned to kick", colour= discord.colour.Color.red())
    await ctx.send(embed= embed)
    return ""
    
  
  # get reason
  
  import re
  
  x = re.search("(<@!\d+>) ?(.*)", msg)
  if x != None:
    # print("Mention: " + x.group(1))
    reason = ("reason: " + x.group(2))
    print(reason)

    if reason == "reason: ":
      reason = "reason: None"
    
    await ctx.send("Pretend "+ target.name + " is kicked for " + reason)

   
'''
  if message.author.
    try:
      await target.kick(reason= reason)

      embed = discord.Embed(title= "User Kicked", description= f"{target.name}.exe has been moved to the recycle bin", colour= discord.colour.Colour.green())
      embed.set_author(name= "Programers Princess", icon_url= ppLogo)
      embed.set_thumbnail(url= target.avatar_url)
      await ctx.send(embed= embed)
    
    except discord.Forbidden:
      embed= discord.Embed(title= "Error", description= "I don't have permission to kick this person", colour= discord.colour.Color.red())
      await ctx.send(embed= embed)
  else:
    pass
'''














def run_client():
  client.run("Token")

run_client()