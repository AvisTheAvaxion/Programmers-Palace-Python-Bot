from abc import abstractmethod
import os
import re
import time
import traceback
from os.path import dirname, join
import discord
from dotenv import load_dotenv

from logger import Logger, LogLevel

# Load Logger
log = Logger(LogLevel.DEBUG)

# Loads Environment Variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Sets Intents
intents = discord.Intents.default()
intents.members = True

# Constants
version = "A0.0.5"
#prefix = os.environ.get("prefix")
prefix = ">"

links = {
  'logo': 'https://cdn.discordapp.com/avatars/823751670210363393/472d53a711b5fe4393b6bc5dc9f6e47a.webp?size=2048',
  'justask': 'https://media.discordapp.net/attachments/767475855990456363/823756179812646922/unknown.png',
  'googleit': 'https://media.discordapp.net/attachments/267131764827357184/823690855864991744/unknown.png',
  'invite': 'https://discord.gg/jP4urjM'
}

user = {
  'Doomer': '756757056941326397',
  'Avis': '364905148083994626'
}


staff = {
  299210434467069963: "Canter",
  66609022161133568: "Duke",
  136214966804938752: "Jordan",
  269707833916915723: "Lutz",
  184641676457803777: "Sammie",
  297167297708032010: "Troll",
  364905148083994626: "Avis",
  756757056941326397: "Doomer",
  328871569881563137: "GL4SS",
  164952144368107520: "TECA",
  327489637176311810: "Random",
  539910274698969088: "Wesam"
}



# Client Class
class PPClient(discord.Client):
  def __init__(self, intents):
    super(PPClient, self).__init__(intents=intents)
    self.commands = []

  def add_command(self, command):
    self.commands.append(command)

  async def on_ready(self):
    activity = discord.Game(name=f" with code |>help |{version}")
    await client.change_presence(status=discord.Status.online, activity=activity)
    log.clear()
    log.log("Programmers Princess Bot is ready!", LogLevel.INFO)

  async def on_member_join(self, member):
    channel = await client.fetch_channel(823960806260604928)
    embed = discord.Embed(title= f"{member.name} Joined!", description= f"{member.name}.exe has been sucessfully downloaded!", colour= discord.colour.Color.blue())
    embed.set_author(name= "Programers Princess", icon_url= links['logo'])
    embed.set_thumbnail(url= member.avatar_url)
    await channel.send(embed= embed)
  
  async def on_member_remove(self, member):
    channel = await client.fetch_channel(823960806260604928)
    embed = discord.Embed(title= f"{member.name} Left!", description= f"{member.name}.exe deleted themselves.", colour= discord.colour.Color.blue())
    embed.set_author(name= "Programers Princess", icon_url= links['logo'])
    embed.set_thumbnail(url= member.avatar_url)
    await channel.send(embed= embed)
  
  async def on_message(self, message):
    if message.content.lower() == "typescript":
      await message.channel.send("is trash")
    elif(message.content.startswith(prefix)):
      message.content = message.content[len(prefix):]
      keyword = message.content.split(' ')[0]
      for cmd in self.commands:
        for alias in cmd.name:
          if(alias == keyword):
            log.log(f'{message.author} triggered {cmd.name[0]} via {alias}!', LogLevel.DEBUG)
            await cmd.execute(message)


# Client Object
client = PPClient(intents=intents)

# Command Template
class Command():
  def __init__(self, name, run, help):
    if isinstance(name, list):
      self.name = name
    else:
      self.name = [ name ]
    self.run = run
    self.help = help
    client.add_command(self)

  @abstractmethod
  async def execute(self, mesg):
    await self.run(mesg)


# Ping Method
async def ping(mesg):
  tic = time.perf_counter()
  latency = client.latency
  msg = await mesg.channel.send("*Computing Latency*")
  toc = time.perf_counter()
  await msg.edit(content= f"Pong: {round(latency * 1000)}ms | {(toc - tic) * 1000:0.0f}ms")
ping_cmd = Command('ping', ping, 'returns the latency!')

# Help Command (has to be last)
async def help(mesg):
  embed = discord.Embed(title = "Help", description = "You asked for help", colour = discord.colour.Color.green())
  embed.set_author(name= "Programers Princess", icon_url= links['logo'])
  for cmd in client.commands:
    if(not(cmd.help == None)):
      embed.add_field(name = f"{prefix}{cmd.name[0]}", value = cmd.help, inline = False)
  embed.set_footer(text = "Tip or something here?")
  await mesg.reply(embed=embed)
help_cmd = Command('help', help, 'shows the help message!')

# Test Command
async def test(mesg):
  a = await mesg.channel.send("hi")
  await a.edit(content="Test Passed!")
test_cmd = Command('test', test, None)

# Just Ask Command
async def justask(mesg):
  await mesg.channel.send(links['justask'])
  await mesg.delete()
ja_cmd = Command(['justask', 'ja'], justask, 'prints the just ask emoji.')

# Google It Command
async def googleit(mesg):
  await mesg.channel.send(links['googleit'])
  await mesg.delete()
g_cmd = Command(['googleit', 'g'], googleit, 'prints the google it emoji.')

# Invite Command
async def invite(mesg):
  await mesg.channel.send(links['invite'])
  await mesg.delete()
invite_cmd = Command('invite', invite, 'sends an invite!')

# Report Command
async def report(mesg):
  msg = mesg.content
  report = msg[(len('report')+1):]
  Doomer = await client.fetch_user(user['Doomer'])

  doomerEmbed = discord.Embed(title= "New Report", description= report, colour= discord.colour.Color.red())
  doomerEmbed.set_author(name= mesg.author.name, icon_url= mesg.author.avatar_url)
  await Doomer.send(embed = doomerEmbed)

  channelEmbed = discord.Embed(title = "Report Submitted!", description= report, colour= discord.colour.Color.green())
  channelEmbed.set_author(name = mesg.author.name, icon_url= mesg.author.avatar_url)
  await mesg.channel.send(embed = channelEmbed)
report_cmd = Command('report', report, 'report a bug!')

# Nick Command
async def nick(mesg):
  try:
    msg = mesg.content
    nickname = msg[(len('nick')+1):]
    user = mesg.author
    
    if nickname == "clear":
      print('Reached Clear')
      await user.edit(nick = None)
      embed = discord.Embed(title = "Nickname Cleared!", description = "Your nickname has been cleared!", colour = discord.colour.Color.green())
      embed.set_author(name = "Programmers Princess", icon_url = links['logo'])
      msg = await mesg.send(embed = embed)
      await msg.delete(delay = 3)
    else:
      print('Reached Nick')
      await user.edit(nick = nickname)
      embed = discord.Embed(title="Nickname Changed!", description= f"Your nickname has been changed to {nickname}!", colour= discord.colour.Color.green())
      embed.set_author(name= "Programers Princess", icon_url= links['logo'])
      msg = await mesg.channel.send(embed= embed)
  except discord.Forbidden:
    embed = discord.Embed(title="Error", description= "I don't have permission to change your nickname!", colour= discord.colour.Color.red())
    embed.set_author(name= "Programers Princess", icon_url= links['logo'])
    msg = await mesg.channel.send(embed= embed)
nick_cmd = Command('nick', nick, 'changes nick!')

# Kick Command
async def kick(mesg):
  msg = mesg.content
  try:
    target = mesg.mentions[0]
  except IndexError:
    embed = discord.Embed(title= "Error", description= "No member mentioned to kick", colour= discord.colour.Color.red())
    await mesg.channel.send(embed = embed)
    return ""
  
  x = re.search("<@!\d+> ?(.*)", msg)
  if x != None:
    text = f'{target.name}.exe was sent to the recyling bin with the php files'
    if x.group(1) == "":
      text += "!"
      reason = "None"
    else:
      text += (" for: " + x.group(1))
      reason = x.group(1)
    
    if target.id in staff:
      embed = discord.Embed(title= "Error", description= "You can't kick staff members", colour= discord.colour.Color.red())
      await mesg.channel.send(embed= embed)

      if target.id == 299210434467069963:
        await mesg.channel.send("https://static.wikia.nocookie.net/24005259-b85f-4770-a051-abadd75daace")
        
    else:
      try:
        await target.kick(reason= reason)
        await mesg.channel.send(text)

      except discord.Forbidden:
        embed = discord.Embed(title= "Error", description= "I don't have permission to kick this person", colour= discord.colour.Color.red())
        await mesg.channel.send(embed= embed)
kick_cmd = Command('kick', kick, 'kicks a user!')


# Ban Command
async def ban(mesg):
  msg = mesg.content
  try:
    target = mesg.mentions[0]
  except IndexError:
    embed = discord.Embed(title= "Error", description= "No member mentioned to ban", colour= discord.colour.Color.red())
    await mesg.channel.send(embed = embed)
    return ""
  
  x = re.search("<@!\d+> ?(.*)", msg)
  if x != None:
    text = f'{target.name} code was scrambled beyond recognition'
    if x.group(1) == "":
      text += "!"
      reason = "None"
    else:
      text += (" for: " + x.group(1))
      reason = x.group(1)
    
    if target.id in staff:
      embed = discord.Embed(title= "Error", description= "You can't ban staff members", colour= discord.colour.Color.red())
      await mesg.channel.send(embed= embed)

      if target.id == 299210434467069963:
        await mesg.channel.send("https://static.wikia.nocookie.net/24005259-b85f-4770-a051-abadd75daace")
        
    else:
      try:
        await target.ban(reason= reason)
        await mesg.channel.send(text)

      except discord.Forbidden:
        embed = discord.Embed(title= "Error", description= "I don't have permission to ban this person", colour= discord.colour.Color.red())
        await mesg.channel.send(embed= embed)
ban_cmd = Command('ban', ban, 'bans a user!')








# Shutdown Command
async def shutdown(mesg):
  issuer = str(mesg.author.id)
  if(issuer == user['Doomer'] or issuer == user['Avis']):
    log.warn('Bot is shutting down!')
    await mesg.add_reaction("✅")
    await client.close()
    log.warn("Bot shutdown complete")

  else:
    embed = discord.Embed(title="Error", description= "You don't have the permission to perform this action!", colour= discord.colour.Color.red())
    embed.set_author(name= "Programers Princess", icon_url= links['logo'])
    await mesg.channel.send(embed = embed)
shutdown_cmd = Command('shutdown', shutdown, None)


# Bot Login
client.run("Token")