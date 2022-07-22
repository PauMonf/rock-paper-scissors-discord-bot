import discord
from discord.ext import commands

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
    if (value == "rock"):
        await ctx.send("Paper")
        await ctx.send("Paper beats rock, I WIN!")
    if (value == "paper"):
        await ctx.send("Scissors")
        await ctx.send("Scissors beats paper, I WIN!")
    if value == "scissors":
        await ctx.send("Rock")
        await ctx.send("Rock beats scissors, I WIN!")


bot.run(TOKEN)
