from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()
from discord.ext import commands

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix='PREFIX',intents = discord.Intents.all())


@bot.event
async def on_ready():
    print("준비 완료!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("!도움을 눌러 대화를 시작해 주세요!"))

@bot.command(name="도움")
async def on_message(ctx):
    await ctx.author.send(embed = discord.Embed(title='도움이 필요하신가요?',description=f"{ctx.message.author.name}님 어떻게 도와드릴까요? 밑에 내용을 보시고 결정 해 주세요!", color=0xf9ff84))
@bot.command(name="거래시작하기")
async def on_message(ctx):
    await ctx.author.send(embed = discord.Embed(title='거래 시작하기',description=f"{ctx.message.author.name}님 거래를 도와드리겠습니다! 거래 봇 개인 채팅창에 !거래를 쳐주세요", color=0xf9ff84))
@bot.command(name="거래방법")
async def on_message(ctx):
    await ctx.author.send(embed = discord.Embed(title='거래 방법',description=f"{ctx.message.author.name}님 어떻게 거래 하는지 모르시겠다고요? 거래 봇 개인 채팅창에 !거래방법을 쳐주세요", color=0xf9ff84))
@bot.command(name="가치표")
async def on_message(ctx):
    await ctx.author.send(embed = discord.Embed(title='가치표',description=f"{ctx.message.author.name}님 아쉽게도 가치표는 아직 업데이트 되지 않았어요ㅠ 업데이트 되면 처음으로 알려 드릴게요!", color=0xf9ff84))
@bot.command(name="거래내역")
async def on_message(ctx):
    await ctx.author.send(embed = discord.Embed(title='거래 내역',description=f"{ctx.message.author.name}님에 대한 거래 내역은 하루 뒤에 전달됩니다!", color=0xf9ff84))
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
