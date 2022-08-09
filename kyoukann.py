# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'とーくん'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if message.content == "p!kyoukann":
        kyoukann=random.randint(1,2)
        if kyoukann == 1:
            await message.channel.send("いや、マジでそれな")
        if kyoukann == 2:
            await message.channel.send("わかる～")
client.run(TOKEN)
