
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


@client.event
async def on_message(message):
  message.content = message.content.lower()
  channel = message.channel

  if message.content ==">help":
     embed = discord.Embed(title= "Help", description= "You asked for help", colour= discord.colour.Color.green())
     embed.set_author(name= "Programers Princess", icon_url= ppLogo)
     embed.add_field(name= ">ja", value= "Displays just ask emoji", inline= False)
     embed.add_field(name= ">g", value= "Displays Google It emoji", inline = False)
     embed.add_field(name= ">invite", value= "Displays a server invite", inline = False)
     embed.add_field(name= ">report [message]", value= "A command to report bugs with the bot", inline = False)
     embed.add_field(name= ">nick [nickname]", value= "Changes your nickname", inline = False)
     embed.add_field(name= ">help", value= "A helpful command", inline= False)
     embed.set_footer(text= "Tip or something here?")
          
     await channel.send(embed= embed)
    
  elif message.content == ">ja":
    await channel.send("https://media.discordapp.net/attachments/767475855990456363/823756179812646922/unknown.png")
    await message.delete()
  
  elif message.content == ">g":
    await channel.send("https://media.discordapp.net/attachments/267131764827357184/823690855864991744/unknown.png")
    await message.delete()
  
  elif message.content == ">invite":
    await channel.send("https://discord.gg/jP4urjM")
    await message.delete()
  
  elif message.content.startswith(">report "):
    msg = message.content
    report = msg[8:]
    Doomer = await client.fetch_user(756757056941326397)

    doomerEmbed = discord.Embed(title= "New Report", description= report, colour= discord.colour.Color.red())
    doomerEmbed.set_author(name= message.author.name, icon_url= message.author.avatar_url)
    await Doomer.send(embed= doomerEmbed)

    channelEmbed = discord.Embed(title= "Report Submitted!", description= report, colour= discord.colour.Color.green())
    channelEmbed.set_author(name= message.author.name, icon_url= message.author.avatar_url)
    await channel.send(embed= channelEmbed)

  
  elif message.content.startswith(">nick "):
    try:
      msg = message.content
      nickname = msg[6:]
      user = message.author
      await user.edit(nick= nickname)
    
      if message.content == ">nick clear":
        await user.edit(nick= None)
        embed = discord.Embed(title="Nickname Cleared!", description= "Your nickname has been cleared!", colour= discord.colour.Color.green())
        embed.set_author(name= "Programers Princess", icon_url= ppLogo)
        msg = await channel.send(embed= embed)
        await msg.delete(delay= 3)

    
      else:
        embed = discord.Embed(title="Nickname Changed!", description= f"Your nickname has been changed to {nickname}!", colour= discord.colour.Color.green())
        embed.set_author(name= "Programers Princess", icon_url= ppLogo)
        msg = await channel.send(embed= embed)
        # await msg.delete(delay= 3)

    except discord.Forbidden:
      embed = discord.Embed(title="Error", description= "I don't have permission to change your nickname!", colour= discord.colour.Color.red())
      embed.set_author(name= "Programers Princess", icon_url= ppLogo)
      msg = await channel.send(embed= embed)

    
  
  elif message.content.startswith(">kick"):
    msg = message.content
    try:
      target = message.mentions[0]
    
    except IndexError:
      embed= discord.Embed(title= "Error", description= "No member mentioned to kick", colour= discord.colour.Color.red())
      await channel.send(embed= embed)
    
    import re
    
    x = re.search("(<@!\d+>) ?(.*)", msg)
    if x != None:
      # print("Mention: " + x.group(1))
      reason = ("Reason: " + x.group(2))
      
      if message.author.
      try:
        await target.kick(reason= reason)

        embed = discord.Embed(title= "User Kicked", description= f"{target.name}.exe has been moved to the recycle bin", colour= discord.colour.Colour.green())
        embed.set_author(name= "Programers Princess", icon_url= ppLogo)
        embed.set_thumbnail(url= target.avatar_url)
        await channel.send(embed= embed)
      
      except discord.Forbidden:
        embed= discord.Embed(title= "Error", description= "I don't have permission to kick this person", colour= discord.colour.Color.red())
        await channel.send(embed= embed)
    else:
      pass
  


client.run("Token")