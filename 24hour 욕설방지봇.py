# -*- coding:utf-8 -*- 
# 가끔가다 애가 인코딩을 잘못 읽어서 오류를 냅니다. 그것을 대비하기 위해 'utf-8'으로 읽으라고 선언함

import discord

 

token = "NzM1MzA3MzQwMzQ5MzA5MDA5.XxeWZg.xy8BqrGUL-r5ytwZLeqGaN5dh4k" #<- 봇 토큰 입력하는곳 
client = discord.Client()

@client.event
async def on_ready(): # 봇이 준비가 되면 1회 실행되는 부분입니다.
  # 봇이 "반갑습니다"를 플레이 하게 됩니다.
  # discord.Status.online에서 online을 dnd로 바꾸면 "다른 용무 중", idle로 바꾸면 "자리 비움"으로 바뀝니다.
  await client.change_presence(status=discord.Status.online, activity=discord.Game("욕방지중..")) #<- 봇 상태 구문
  print("하울") 
  print(client.user.name) 
  print(client.user.id) 

   

badwords = ["시발", "병신", "장애", "섹스", "보지", "자지", "느금마", "니애미", "니애비", "후장", "느금빠", "ㅅㅂ", "지랄", "씨발", "^^ㅣ발", "^^l발", "ㄴㄱㅁ", "ㅗ",] #<-여기에 욕설 등록 시 (단어) 자동으로 삭제 처리함 더추가 가능

@client.event 
async def on_message(message):

    for word in badwords:
        if message.content.count(word) > 0:
            print("욕설이 감지되어 삭제처리 되었습니다. 계속욕설시 추방 합니다.")
            print(message.author.id)
            await message.channel.purge(limit=1)
    for word in badwords:
        author = message.guild.get_member(int(message.author.id))
        if message.content.count(word) > 0:
            await message.channel.send(embed=embed)

            

embed=discord.Embed(title="하울 샵", description="욕설이 감지되어 삭제처리 되었습니다.", color=0xCC0045) #<- 임베드 구문 



client.run(token)








  

client.run(token)

