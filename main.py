#BU KODU NASIL YAPTIĞIMI KİMSE BİLMİYO BEN DAHİL
import asyncio
from discord import channel, client, colour, member, role
from discord.ext import commands
import discord
from discord.ext.commands import bot
import random as r
import os
from discord.ext.commands.core import command
import pyautogui
import time
import contextlib
import io
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType, component
from discord.utils import get
from discord_slash import SlashCommand

client = discord.Client()
intents = discord.Intents(messages = True, guilds= True, reactions = True, members = True, presences = True)
Bot = commands.Bot(command_prefix='*n ',intents = intents)
ddb = DiscordComponents(Bot)
slash = SlashCommand(Bot, sync_commands=True)

def bot_hazır():
    @Bot.event
    async def on_ready():
        await Bot.change_presence(status=discord.Status.idle, activity=discord.Game('*n yardım or /yardım'))
        print("Ben Hazırım...")
        DiscordComponents(Bot)

def giris_cıkıs():
    @Bot.event
    async def on_member_join(member):
        channel = discord.utils.get(member.guild.text_channels, name="📥・giriş-çıkış")
        await channel.send(f"{member} Aramıza Hoşgeldin...")
    @Bot.event
    async def on_member_remove(member):
        channel = discord.utils.get(member.guild.text_channels, name="📥・giriş-çıkış")
        await channel.send(f"{member} Aramızdan ayrıldı. Hoşcakal...")

def gunluk_soz():
    guild_ids = [852913062548733992] 
    @slash.slash(name="söz", 
    guild_ids=guild_ids,
    description="Random Söz Gösterir.")
    async def sözz(ctx):
        liste = ["**Ömür bir masal gibidir, ne kadar uzun olduğu değil, ne kadar güzel yaşandığı önemlidir.**","**Yüzümüzün ve gözlerimizin rengi ne olursa olsun, gözyaşlarımızın rengi aynıdır.**","**Kar taneleri ne güzel anlatıyor, birbirlerine zarar vermeden de yol almanın mümkün olduğunu.**","**Mükеmmеl kişiyi aramaktan vazgеç. Tеk ihtiyacın olan sana sahip olduğu için şanslı olduğunu düşünеn biridir.**","**Mükеmmеl kişiyi aramaktan vazgеç. Tеk ihtiyacın olan sana sahip olduğu için şanslı olduğunu düşünеn biridir.**","**Doğuştan sahip olduklarınızla yaşamayı öğrenmek bir süreç, bir katılım, yani yaşamınızın yoğrulmasıdır.**","**Aşktan korkmak, yaşamdan korkmak demektir ve yaşamdan korkanlar şimdiden üç kez ölmüşlerdir.**","**Bazı insanlar yağmuru hissеdеr, bazıları isе sadеcе ıslanır.**","**Hayattaki en büyük zafer hiçbir zaman düşmemekte değil, her düştüğünde ayağa kalkmakta yatar.**","**İnsanların, senin hakkında ne düşündüklerini önemsemeyerek, ömrünü uzatabilirsin mesela. – Bukowski**","**Unutma; Hеr gеlеn sеvmеz.. Vе hiçbir sеvеn gitmеz. - Nazım Hikmеt**","**Hiç bir canın acısı, sеnin acından az dеğildir.**","**Üstada sorarlar sеvgi mi nеfrеt mi diyе, “nеfrеt” diyе cеvap vеrir vе еklеr; çünkü onun sahtеsi olmaz.**","**Yanlış bildiğin yolda; hеrkеslе yürüyеcеğinе, doğru bildiğin yolda; tеk başına yürü…**","**Büyük sıçrayışı gerçekleştirmek isteyen, birkaç adım geriye gitmek zorundadır. Bugün yarına dünle beslenerek yol alır. Bertolt Brecht**","**Küçük işlere gereğinden çok önem verenler, elinden büyük iş gelmeyenlerdir.Eflatun **","**Mutluluk elin erişebileceği çiçeklerden bir demet yapma sanatıdır.B.Goddar**"]
        söz_ctx = r.choice(liste)
        embed = discord.Embed(
            title = '',
            description = söz_ctx,
            colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)

def gunluk_soz2():
    @Bot.command()
    async def söz(ctx):
        liste = ["**Ömür bir masal gibidir, ne kadar uzun olduğu değil, ne kadar güzel yaşandığı önemlidir.**","**Yüzümüzün ve gözlerimizin rengi ne olursa olsun, gözyaşlarımızın rengi aynıdır.**","**Kar taneleri ne güzel anlatıyor, birbirlerine zarar vermeden de yol almanın mümkün olduğunu.**","**Mükеmmеl kişiyi aramaktan vazgеç. Tеk ihtiyacın olan sana sahip olduğu için şanslı olduğunu düşünеn biridir.**","**Mükеmmеl kişiyi aramaktan vazgеç. Tеk ihtiyacın olan sana sahip olduğu için şanslı olduğunu düşünеn biridir.**","**Doğuştan sahip olduklarınızla yaşamayı öğrenmek bir süreç, bir katılım, yani yaşamınızın yoğrulmasıdır.**","**Aşktan korkmak, yaşamdan korkmak demektir ve yaşamdan korkanlar şimdiden üç kez ölmüşlerdir.**","**Bazı insanlar yağmuru hissеdеr, bazıları isе sadеcе ıslanır.**","**Hayattaki en büyük zafer hiçbir zaman düşmemekte değil, her düştüğünde ayağa kalkmakta yatar.**","**İnsanların, senin hakkında ne düşündüklerini önemsemeyerek, ömrünü uzatabilirsin mesela. – Bukowski**","**Unutma; Hеr gеlеn sеvmеz.. Vе hiçbir sеvеn gitmеz. - Nazım Hikmеt**","**Hiç bir canın acısı, sеnin acından az dеğildir.**","**Üstada sorarlar sеvgi mi nеfrеt mi diyе, “nеfrеt” diyе cеvap vеrir vе еklеr; çünkü onun sahtеsi olmaz.**","**Yanlış bildiğin yolda; hеrkеslе yürüyеcеğinе, doğru bildiğin yolda; tеk başına yürü…**","**Büyük sıçrayışı gerçekleştirmek isteyen, birkaç adım geriye gitmek zorundadır. Bugün yarına dünle beslenerek yol alır. Bertolt Brecht**","**Küçük işlere gereğinden çok önem verenler, elinden büyük iş gelmeyenlerdir.Eflatun **","**Mutluluk elin erişebileceği çiçeklerden bir demet yapma sanatıdır.B.Goddar**"]
        söz_ctx = r.choice(liste)
        embed = discord.Embed(
            title = '',
            description = söz_ctx,
            colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)

def tas_kagıt():
    @Bot.command()
    async def tkm(ctx, *args):
        liste = ["Taş","Kağıt","Makas"]
        bot_secim = r.choice(liste)
        if "Taş" in args:
            if bot_secim == "Taş":
                await ctx.send("> BOTUN SEÇİMİ {TAŞ} BERABERE.")
                await ctx.send('https://tenor.com/view/okay-sad-alright-sad-face-meme-gif-4887561')
            elif bot_secim == "Kağıt":
                await ctx.send("> BOTUN SEÇİMİ {KAĞIT} KAYBETTİNİZ.")
                await ctx.send('https://tenor.com/view/milk-and-mocha-cry-sad-tears-upset-gif-11667710')
            else:
                await ctx.send("> BOTUN SEÇİMİ {MAKAS} KAZANDINIZ.")
                await ctx.send('https://tenor.com/view/spongebob-squarepants-dance-happy-dance-%E6%AD%A1%E5%BF%AB-gif-5084836')
        elif "Kağıt" in args:
            if bot_secim == "Kağıt":
                await ctx.send("> BOTUN SEÇİMİ {KAĞIT} BERABERE.")
                await ctx.send('https://tenor.com/view/okay-sad-alright-sad-face-meme-gif-4887561')
            elif bot_secim == "Taş":
                await ctx.send("> BOTUN SEÇİMİ {TAŞ} KAZANDINIZ.")
                await ctx.send('https://tenor.com/view/spongebob-squarepants-dance-happy-dance-%E6%AD%A1%E5%BF%AB-gif-5084836')
            else:
                await ctx.send("> BOTUN SEÇİMİ {MAKAS} KAYBETTİNİZ.")
                await ctx.send('https://tenor.com/view/milk-and-mocha-cry-sad-tears-upset-gif-11667710')
        elif "Makas" in args:
            if bot_secim == "Makas":
                await ctx.send("> BOTUN SEÇİMİ {MAKAS} BERABERE.")
                await ctx.send('https://tenor.com/view/okay-sad-alright-sad-face-meme-gif-4887561')
            elif bot_secim == "Taş":
                await ctx.send("> BOTUN SEÇİMİ {TAŞ} KAYBETTİNİZ.")
                await ctx.send('https://tenor.com/view/milk-and-mocha-cry-sad-tears-upset-gif-11667710')
            else:
                await ctx.send("> BOTUN SEÇİMİ {KAĞIT} KAZANDINIZ.")
                await ctx.send('https://tenor.com/view/spongebob-squarepants-dance-happy-dance-%E6%AD%A1%E5%BF%AB-gif-5084836')
def screen_shot():
    @Bot.command()
    async def ss(ctx, *args):
        time.sleep(3)
        ekran_goruntusu = pyautogui.screenshot()
        dosya_adi = "ekran_goruntusu.jpg"
        dosya_yolu = os.path.join('C:\\Users\Yiğit Efe\Desktop', dosya_adi)
        ekran_goruntusu.save(dosya_yolu)
        embed = discord.Embed(
            title = 'SCREEN SHOT',
            description = '**Ekran Görüntüsü Alındı !**',
            colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)

def otorol():
    @Bot.event
    async def on_member_join(member):
        role = discord.utils.get(member.guild.roles, name='embed')
        await member.add_roles(role)

def bugun():
    zaman = time.asctime()
    guild_ids = [852913062548733992] 

    @slash.slash(name="bugün", 
    guild_ids=guild_ids,
    description="Bugünün tarihini ve saatini verir.")
    async def bugünn(ctx):
        embed = discord.Embed(
            title = 'TODAY',
            description = f'**Bugün ki zaman : {zaman}**',
            colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)

def bugun2():
    @Bot.command()

    async def bugün(ctx):
        embed = discord.Embed(
            title = 'TODAY',
            description = f'**Bugün ki zaman : {zaman}**',
            colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)

def kickk():
    @Bot.command()
    async def at(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(
            title = 'KİCK',
            description = f'** {member} Sunucudan Atıldı !**',
            colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)

def run_py():
    guild_ids = [852913062548733992] 

    @slash.slash(name="run", 
    guild_ids=guild_ids,
    description="Python kodlarınızı çalıştırmanızı sağlar.")
    async def runn(ctx, *, code):
        str_obj = io.StringIO() 
        try:
            with contextlib.redirect_stdout(str_obj):
                exec(code)
        except Exception as e:
            return await ctx.send(f"```{e.__class__.__name__}: {e}```")
        embed = discord.Embed(
            title = 'PYTHON',
            description = f'**{str_obj.getvalue()}**',
            colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)


def run_py2():
    @Bot.command()
    async def run(ctx, *, code):
        str_obj = io.StringIO() 
        try:
            with contextlib.redirect_stdout(str_obj):
                exec(code)
        except Exception as e:
            return await ctx.send(f"```{e.__class__.__name__}: {e}```")
        embed = discord.Embed(
            title = 'PYTHON',
            description = f'**{str_obj.getvalue()}**',
            colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)

def mesaj_sil():
    @Bot.command()
    async def sil(ctx, amount = 5):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(
            title = 'DELETE',
            description = f'**{amount} Mesaj Silindi**',
            colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)

def mesaj_gönderme():
    guild_ids = [852913062548733992] 

    @slash.slash(name="özel_mesaj", 
    guild_ids=guild_ids,
    description="Etiketlediğiniz kullanıcya istediğiniz mesajı gönderir.")
    async def özel_mesajj(ctx, member: discord.Member, *, content):
        channel = await member.create_dm()
        await channel.send(content)
        embed = discord.Embed(
            title = 'SEND MESSAGE',
            description = f'**{member} Kişisine Mesaj Gönderildi !**',
            colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)

def mesaj_gönderme2():
    @Bot.command()
    async def özel_mesaj(ctx, member: discord.Member, *, content):
        channel = await member.create_dm()
        await channel.send(content)
        embed = discord.Embed(
            title = 'SEND MESSAGE',
            description = f'**{member} Kişisine Mesaj Gönderildi !**',
            colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)

def sosyal_button():
    guild_ids = [852913062548733992] 

    @slash.slash(name="sosyal", 
    guild_ids=guild_ids,
    description="Geliştiricinin sosyal-medya hesaplarını gösterir.")
    async def sosyall(ctx):
        await ctx.channel.send("> Sosyal-Medya Hesaplarım",
            components=[
                Button(style=ButtonStyle.URL, url='https://www.youtube.com/channel/UCckOewpr_RoPDohesBGXXDA', label="Youtube"),
                Button(style=ButtonStyle.URL, url='https://www.instagram.com/nyks_yigit1/', label="Instagram"),
                Button(style=ButtonStyle.URL, url='https://discord.gg/UgANSCVz2Q', label="Discord Sunucum"),
                # Button(style=ButtonStyle.blue,label="Discord Sunucum"),
            ]
        )
        # res = await Bot.wait_for("button_click")
        # if res.channel == ctx.channel:
        #     print("Çalıştı 1")
        # res2 = await client.wait_for("button_click")
        # if res.channel == ctx.channel:
        #     print("Çalıştı 2")

def sosyal_button2():
    @Bot.command()
    async def sosyal(ctx):
        await ctx.channel.send("> Sosyal-Medya Hesaplarım",
            components=[
                Button(style=ButtonStyle.URL, url='https://www.youtube.com/channel/UCckOewpr_RoPDohesBGXXDA', label="Youtube"),
                Button(style=ButtonStyle.URL, url='https://www.instagram.com/nyks_yigit1/', label="Instagram"),
                Button(style=ButtonStyle.URL, url='https://discord.gg/UgANSCVz2Q', label="Discord Sunucum"),
                # Button(style=ButtonStyle.blue,label="Discord Sunucum"),
            ]
        )
        # res = await Bot.wait_for("button_click")
        # if res.channel == ctx.channel:
        #     print("Çalıştı 1")
        # res2 = await client.wait_for("button_click")
        # if res.channel == ctx.channel:
        #     print("Çalıştı 2")

def komutlar():
    guild_ids = [852913062548733992] 

    @slash.slash(name="yardım", 
    guild_ids=guild_ids,
    description="Kullanabileceğiniz tüm komutları gösterir.")
    async def yardımm(ctx):
        embed = discord.Embed(
            title = '> KOMUTLAR LİSTESİ',
            description = """```fix
*n söz (Rastgele sözler yazar)
```
```fix
*n tkm [seçim] (Taş, Kağıt, Makas belirttiğiniz takdirde oyun başlar)
```
```fix
*n ss (3 saniye sonrasında ekran görüntüsü alır)
```
```fix
*n bugün (Bugünün tarihini ve saatini verir)
```
```fix
*n at [@kişi] (Etiketlediğiniz kişi sunucudan atılır)
```
```fix
*n run [komut] (Yazdığınız python kodlarını çalıştırır)
```    
```fix
*n sil [miktar] (Belirttiğiniz miktarda mesaj siler)
```      
```fix
*n özel_mesaj [@kullanıcı] [mesajınız] (Yazdığınız mesajı etiketlediğiniz kişiye bot hesabından gönderir)
```
```fix
*n sosyal (Programcının sosyal-medya hesaplarına ulaşırsınız)
```
```fix
*n avatar [@kullanıcı] (Etiketlediğiniz kullanıcının profil fotoğrafını görürsünüz)
```
```fix
*n ping (Anlık gecikme sürenizi gösterir)
```
```fix
*n ban [@kullanıcı] ['saniye's] (Belirttiğiniz süre içinde ban yer ve sunucudan atılır)
```


            """,
            colour = discord.Colour.blue()
        )
        embed.set_footer(text='Nyks Bot')
        embed.set_image(url='https://contenthub-static.grammarly.com/blog/wp-content/uploads/2018/05/how-to-ask-for-help-760x400.jpg')
        await ctx.send(embed=embed)

def komutlar2():
    @Bot.command()
    async def yardım(ctx):
        embed = discord.Embed(
            title = '> KOMUTLAR LİSTESİ',
            description = """```fix
*n söz (Rastgele sözler yazar)
```
```fix
*n tkm [seçim] (Taş, Kağıt, Makas belirttiğiniz takdirde oyun başlar)
```
```fix
*n ss (3 saniye sonrasında ekran görüntüsü alır)
```
```fix
*n bugün (Bugünün tarihini ve saatini verir)
```
```fix
*n at [@kişi] (Etiketlediğiniz kişi sunucudan atılır)
```
```fix
*n run [komut] (Yazdığınız python kodlarını çalıştırır)
```    
```fix
*n sil [miktar] (Belirttiğiniz miktarda mesaj siler)
```      
```fix
*n özel_mesaj [@kullanıcı] [mesajınız] (Yazdığınız mesajı etiketlediğiniz kişiye bot hesabından gönderir)
```
```fix
*n sosyal (Programcının sosyal-medya hesaplarına ulaşırsınız)
```
```fix
*n avatar [@kullanıcı] (Etiketlediğiniz kullanıcının profil fotoğrafını görürsünüz)
```
```fix
*n ping (Anlık gecikme sürenizi gösterir)
```
```fix
*n ban [@kullanıcı] ['saniye's] (Belirttiğiniz süre içinde ban yer ve sunucudan atılır)
```


            """,
            colour = discord.Colour.blue()
        )
        embed.set_footer(text='Nyks Bot')
        embed.set_image(url='https://contenthub-static.grammarly.com/blog/wp-content/uploads/2018/05/how-to-ask-for-help-760x400.jpg')
        await ctx.send(embed=embed)


def profile_member():
    guild_ids = [852913062548733992] 

    @slash.slash(name="avatar", 
    guild_ids=guild_ids,
    description="Eiketlediğiniz kullanıcın profil fotoğrafını gösterir.")
    async def avatar(ctx,member: discord.Member):
        embed = discord.Embed(
            title = 'USER PROFİLE PHOTO',
            colour = discord.Colour.green(),
        )
        embed.set_image(url='{}'.format(member.avatar_url))
        await ctx.send(embed=embed)

def profile_member2():
    @Bot.command()
    async def avatar(ctx,member: discord.Member):
        embed = discord.Embed(
            title = 'USER PROFİLE PHOTO',
            colour = discord.Colour.green(),
        )
        embed.set_image(url='{}'.format(member.avatar_url))
        await ctx.send(embed=embed)

def pingg():
    guild_ids = [852913062548733992] 

    @slash.slash(name="ping", 
    guild_ids=guild_ids,
    description="Anlık gecikmenizi söyler.")
    async def pingg(ctx: commands.Context):
        embed = discord.Embed(
            title = '**GECİKME SÜRESİ**',
            colour = discord.Colour.green(),
            description = round(Bot.latency,1000),
        )
        await ctx.send(embed=embed)

def pingg2():
    @Bot.command()
    async def ping(ctx: commands.Context):
        embed = discord.Embed(
            title = '**GECİKME SÜRESİ**',
            colour = discord.Colour.green(),
            description = round(Bot.latency,1000),
        )
        await ctx.send(embed=embed)

def arg_error():
    @Bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title = "EKSİK KOMUT",
                colour = discord.Colour.red(),
                description = "**[*n yardım] YAZARAK KOMUTLARI GÖZDEN GEÇİRİNİZ !**"
            )
            embed.set_image(url='https://miro.medium.com/max/4934/1*AOWyQTPcLQBwM-aD0AfABA.png')
            await ctx.send(embed=embed)

class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]

        if amount.isdigit() and unit in ['s', 'm']:
            return (int(amount), unit)

        raise commands.BadArgument(message='Not a valid duration ')

def second_ban():
    @Bot.command()
    async def ban(ctx, member: commands.MemberConverter, duration: DurationConverter):
        multiplier = {'s': 1, 'm': 60}
        amount, unit = duration
        await ctx.guild.ban(member)
        embed = discord.Embed(
            title = 'SECOND BAN',
            colour = discord.Colour.red(),
            description = f'**[{member} ]KULLANICISI [{amount}] SANİYE BAN YEDİ**'
        )
        await ctx.send(embed=embed)
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)

def run():
    bot_hazır()
    giris_cıkıs()
    gunluk_soz()
    tas_kagıt()
    screen_shot()
    otorol()
    bugun()
    kickk()
    run_py()
    mesaj_sil()
    mesaj_gönderme()
    sosyal_button()
    komutlar()
    profile_member()
    pingg()
    arg_error()
    second_ban()
    gunluk_soz2()
    bugun2()
    run_py2()
    mesaj_gönderme2()
    sosyal_button2()
    komutlar2()
    profile_member2()
    pingg2()
run()
Bot.run('')
