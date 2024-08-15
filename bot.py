import discord
from discord.ext import commands
import passwen

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="&&", intents=intents)

async def on_ready():
    print(f"Hemos iniciado sesión como {bot.user}")

@bot.command(name = "hi")
async def hi(ctx, nombre):
    await ctx.send(f"Hello, my name is: {bot.user.name}, I'm pleasure to talk with ya' {nombre}")

@bot.command(name1 = "passgen")
async def passgen(ctx, i:int):
  await passwen.gen_pass(i)
    

bot.run("")

#this is old code
#client = discord.Client(intents=intents)
#@client.event
  
#async def on_message(message):

 #   if message.author == client.user :
  #      return
   # if message.content.startswith("!hello"):
  #      await message.channel.send("HI!!!!11!11") 
   # elif message.content.startswith('!bye'):
  #      await message.channel.send("I'm sad by hearing that...")
   # else:
    #    await message.channel.send(message.content)
