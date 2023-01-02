from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()
from discord.ui import Button, View
from discord.ext import commands

bot = commands.Bot(command_prefix='PREFIX',intents = discord.Intents.all())


@bot.event
async def on_ready():
    print("준비 완료!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("!도움을 눌러 대화를 시작해 주세요!"))
@bot.command(name="777안내")
async def on_message(ctx):
    ch1 = bot.get_channel(1059028354113744937)
    await ch1.send("관리자 봇을 사용하려면 채팅창에 !도움을 쳐주세요")
@bot.command(name="도움")
async def 버튼(ctx):
    button1 = Button(label="거래", style = discord.ButtonStyle.green)
    button2 = Button(label="거래 방법", style = discord.ButtonStyle.green)
    button3 = Button(label="가치표", style = discord.ButtonStyle.green)
    button4 = Button(label="거래내역", style = discord.ButtonStyle.green)

    async def button_callback1(interaction):
        await ctx.author.send(embed = discord.Embed(title='거래 시작하기',description=f"{ctx.message.author.name}님 거래를 도와드리겠습니다! 거래 봇 개인 채팅창에 !거래를 쳐주세요", color=0xf9ff84))
        print(f"{ctx.message.author.name}님이 거래 버튼을 눌렀습니다")
    async def button_callback2(interaction):
        await ctx.author.send(embed = discord.Embed(title='거래 방법',description=f"{ctx.message.author.name}님 어떻게 거래 하는지 모르시겠다고요? 거래 봇 개인 채팅창에 !거래방법을 쳐주세요", color=0xf9ff84))
        print(f"{ctx.message.author.name}님이 거래방법 버튼을 눌렀습니다")
    async def button_callback3(interaction):
        await ctx.author.send(embed = discord.Embed(title='가치표',description=f"{ctx.message.author.name}님 아쉽게도 가치표는 아직 업데이트 되지 않았어요ㅠ 업데이트 되면 처음으로 알려 드릴게요!", color=0xf9ff84))
        print(f"{ctx.message.author.name}님이 가치표 버튼을 눌렀습니다")
    async def button_callback4(interaction):
        await ctx.author.send(embed = discord.Embed(title='거래 내역',description=f"{ctx.message.author.name}님에 대한 거래 내역은 하루 뒤에 전달됩니다!", color=0xf9ff84))
        print(f"{ctx.message.author.name}님이 거래 내역 버튼을 눌렀습니다")

    button1.callback = button_callback1
    button2.callback = button_callback2
    button3.callback = button_callback3
    button4.callback = button_callback4

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    await ctx.author.send(embed = discord.Embed(title='도움이 필요하신가요?',description=f"{ctx.message.author.name}님 어떻게 도와드릴까요? 밑에 버튼을 클릭하면 도와드릴 수 있어요!", color=0xf9ff84), view=view)
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
