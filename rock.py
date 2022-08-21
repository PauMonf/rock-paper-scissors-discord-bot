import discord
from discord.ext import commands
import random

TOKEN = ""

description = "Rock, paper, scissors, SHOOT!"
bot = commands.Bot(command_prefix="ñ", description=description)


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")
    game = discord.Game("Rock, paper, scissors")
    await bot.change_presence(activity=game)


@bot.command()
async def play(ctx, input):
    value = str(input)
    
    rand=[0,1]
    op=random.choice(rand)
    
    rock=["rock","ROCK","Rock"]
    paper=["paper","PAPER","Paper"]
    scissors=["scissors","SCISSORS","Scissors"]
    
    if (value in rock):
        if (op==0):
            await ctx.send("Paper")
            await ctx.send("Paper beats rock, I WIN!")
        else:
            await ctx.send("Rock")
            await ctx.send("It's a tie ╮(￣ω￣;)╭")
    if (value in paper):
        if (op==0):
            await ctx.send("Scissors")
            await ctx.send("Scissors beats paper, I WIN!")
        else:
            await ctx.send("Paper")
            await ctx.send("It's a tie ╮(￣ω￣;)╭")
    if (value in scissors):
        if (op==0):
            await ctx.send("Rock")
            await ctx.send("Rock beats scissors, I WIN!")
        else:
            await ctx.send("Scissors")
            await ctx.send("It's a tie ╮(￣ω￣;)╭")

bot.run(TOKEN)
