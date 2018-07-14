import discord
import asyncio
from random import randint

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


#ようわからん
users = {}

@client.event
async def on_message(message):
    if message.content == "set user coin":
        if not message.author.id in users.keys():
            users[message.author.id] = 0 #0はコインの数
            await client.send_message(message.channel, "セットしたよ")
        else:
                    await client.send_message(message.channel, "もうあるよ")

@client.event
async def on_message(message):
    if message.content == '!fuck' :
        await client.send_message(message.channel, 'FUCK OFF {}!'.format(message.author.name))

    elif message.content == 'みきりし':
        await client.send_message(message.channel, 'いきりしだよ全くこれだからnoobは'.format(message.author.name))

    elif message.content == "は？" :
        await client.send_message(message.channel, '怒んないで{}ちゃん :heart:'.format(message.author.name))

#dice(1)
    elif message.content == "!dice":
        d = randint(1, 6)
        await client.send_message(message.channel, f"**{d}が出ました！**")

@client.event
async def on_message(message):
    Sh_nezikin_ = ["No Rank", 0]
    Crane0512 = ["No Rank", 0]
    yuta1211 = ["No Rank", 0]
    syunseki = ["No Rank", 0]
    himajima = ["No Rank", 0]
    ODANGO1012 = ["No Rank", 0]
    Yomi_aya = ["No Rank", 0]
    LagiacrusTaishi = ["No Rank", 0]
    mikirisi = ["No Rank", 0]
    you91415519 = ["No Rank", 0]
    waka3126 = ["No Rank", 0]
    tetti_00 = ["No Rank", 0]
    hasuina = ["No Rank", 0]
    kome628 = ["No Rank", 0]

    if message.content == "!help":
        await client.send_message(message.channel, """**丸石会社ネザーラック計算BOT -- HELP**
        使用可能なユーザー : ```Sh_nezikin_, Crane0512, yuta1211, syunseki, himajima, ODANGO1012, Yomi_aya, LagiacrusTaishi, mikirisi, you91415519, waka3126, tetti_00, hasuina, kome628```
        ※ユーザー追加は手動で行っておりますので、```@みたらしだんご#9788```までお問い合わせください
        ~コマンド一覧~
        !help ... このコマンドです
        !check ... 自分の納品数、レベル等を確認します
        !info ... 会社全体の納品数などの情報を確認します
        !add (社長+副社長のみ) ... 社員の納品数を追加します
        !chance (社長+副社長のみ)... ネザーチャンスルーレットをします
        !check admin (社長+副社長のみ) ... 社員全員の納品数、レベル等を確認します。また納品数等の修正も行えます。
        """)

    elif message.content == "!check":
        if message.author.name == "Sh_nezikin_":
            await client.send_message(message.channel, """MCID: Sh_nezikin_
            ランク: {0}
            納品数: {1}""".format(Sh_nezikin_[0],Sh_nezikin_[1]))
        elif message.author.name == "Crane_今日もいい天気":
            await client.send_message(message.channel, """MCID: Crane0512
            ランク: {0}
            納品数: {1}""".format(Crane0512[0],Crane0512[1]))
        elif message.author.name == "ゆた/yuta1211":
            await client.send_message(message.channel, """MCID: yuta1211
            ランク: {0}
            納品数: {1}""".format(yuta1211[0],yuta1211[1]))
        elif message.author.name == "親愛なる戚":
            await client.send_message(message.channel, """MCID: syunseki
            ランク: {0}
            納品数: {1}""".format(syunseki[0],syunseki[1]))
        elif message.author.name == "ひまじま":
            await client.send_message(message.channel, """MCID: himajima
            ランク: {0}
            納品数: {1}""".format(himajima[0],himajima[1]))
        elif message.author.name == "みたらしだんご":
            await client.send_message(message.channel, """MCID: ODANGO1012
            ランク: {0}
            納品数: {1}""".format(ODANGO1012[0],ODANGO1012[1]))
        elif message.author.name == "あやさん":
            await client.send_message(message.channel, """MCID: Yomi_aya
            ランク: {0}
            納品数: {1}""".format(Yomi_aya[0],Yomi_aya[1]))
        elif message.author.name == "LagiacrusTaishi":
            await client.send_message(message.channel, """MCID: LagiacrusTaishi
            ランク: {0}
            納品数: {1}""".format(LagiacrusTaishi[0],LagiacrusTaishi[1]))
        elif message.author.name == "誕生日が夏休みなので呪われたことがある":
            await client.send_message(message.channel, """MCID: mikirisi
            ランク: {0}
            納品数: {1}""".format(mikirisi[0],mikirisi[1]))
        elif message.author.name == "you91415519":
            await client.send_message(message.channel, """MCID: you91415519
            ランク: {0}
            納品数: {1}""".format(you91415519[0],you91415519[1]))
        elif message.author.name == "わか/waka3126":
            await client.send_message(message.channel, """MCID: waka3126
            ランク: {0}
            納品数: {1}""".format(waka3126[0],waka3126[1]))
        elif message.author.name == "tetti_oo/てっち":
            await client.send_message(message.channel, """MCID: tetti_00
            ランク: {0}
            納品数: {1}""".format(tetti_00[0],tetti_00[1]))
        elif message.author.name == "はすいな":
            await client.send_message(message.channel, """MCID: hasuina
            ランク: {0}
            納品数: {1}""".format(hasuina[0],hasuina[1]))
        elif message.author.name == "疫病神":
            await client.send_message(message.channel, """MCID: kome628
            ランク: {0}
            納品数: {1}""".format(kome628[0],kome628[1]))
        #2018/7/13時点
        else:
            await client.send_message(message.channel, """**ERROR:未登録**
            あなたはまだこのBOTのユーザーとして登録されていない状態 or 登録当時の名前と現在のdiscordの名前が違う -- @みたらしだんご#9788まで お問い合わせください""")
    






























client.run('NDYwMzQyNzU5MjUzOTk5NjE2.DhDeDw.fGEy9PhUEFQze3qmLDKF11lZqFw')
