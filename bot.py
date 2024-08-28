import discord
from discord.ext import commands
import passwen
import os, random, requests
#import Extensions.cntrs as ab

#this indicates old code
#client = discord.Client(intents=intents)
#@client.event

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="&&", intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
###

async def on_ready():
  print(f"Bot loggued in as {bot.user}")

@bot.command(name = "hi")
async def hi(ctx, nombre):
    await ctx.send(f"Hello, my name is: {bot.user.name}, I'm pleasure to talk with ya' {nombre}")

@bot.command(name = "passgen")
async def passgen(ctx, i):
  await ctx.send(passwen.gen_pass(int(i)))
    
@bot.command(name = "weed")
async def weed(ctx):
   with open("Discord/random_images/weed.jpg","rb") as img:
      picture = discord.File(img)
   await ctx.send(file = picture)

@bot.command(name = "img")
async def randomimg(ctx):
   j = random.choice(os.listdir("discord/random_images"))
   with open(f"discord/random_images/{j}","rb") as img:
      picture = discord.File(img)
   await ctx.send(file = picture)

@bot.command(name = "duck")
async def ducky(ctx):
  img1 = get_duck_image_url()
  await ctx.send(img1)

bot.run(TOKEN)
