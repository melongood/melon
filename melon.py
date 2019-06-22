from typing import Optional, Any

import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("커뮤니티/사장님월급주세요)")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    global author
    if message.content.startswith("!도움말"):
        await message.channel.send("아직은베타라 명령어가없습니다 삐삑")

    if message.content.startswith("!채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await  client.get_channel(int(channel)).send(msg)

    if message.content.startswith("/뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await  author.add_roles(role)

    if message.content.startswith("/dm"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

client.run("NTg5NjAyMjQzMjA0ODc0MjQw.XQWD9w.FeUj6T7nBK4k8dhuXyTxvNYyGuQ")
