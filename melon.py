from typing import Optional, Any

import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("멜룬")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message, choicenumber=None):
    global author
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")

    if message.content.startswith("!도움말"):
        await message.channel.send("아직은테스트중이라 명령어가별로 없습니다 1.!안녕리고하면 봇이 인사를해줍니다 2.!멜룬은?,!산삼은?,!하넬은?등등하면은 재밌는답을해줍니다 ")

    if message.content.startswith("!멜룬은?"):
        await message.channel.send("존맛탱")

    if message.content.startswith("!산삼은?"):
        await message.channel.send("영양분")

    if message.content.startswith("!하넬은?"):
        await message.channel.send("하넬....어어어어")

    if message.content.startswith("!채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await  client.get_channel(int(channel)).send(msg)

    if message.content.startswith("/뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await  author.add_roles(role)

client.run("NTg4NjYzMjE3MDMxNDc5MzE2.XQRXig.DKzsr3EoMEzf9ZuV_zMlFPFXf8o")
