import discord
from discord.ext import commands
from config import token 
from logic import Pokemon, wizard, fighter
import random

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True 
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('my creator is so cool')
    print('''W.D. Gaster in Deltarune
Built it all from an empty room
Mike the Cat, yeah that is Gaster
Even the Titan that is Gaster
In the bunker sits that Gaster
Entry 17's own master
Kris is Gaster
Susie Gaster
Noelle Gaster
All are Gaster
The Knight is an amalgamate made by Gaster intricate
Gaster is actually green
Dad of Sans and Paps I mean
He fell into his own machine
Split to atoms quite a scene
He's a legend immune to ruin
So he created Deltarune
Dess is missing, that is Gaster
Dark world also surely Gaster
And the vessel that we loot
Well that is also Gaster's doom
And actually damn Deltarune that is also fucking Gaster''')
@bot.command()
async def go(ctx):
    author = ctx.author.name 
    if author not in Pokemon.pokemons:
        chance = random.randint(1, 3)
        if chance == 1:
            pokemon = Pokemon(author)  
        elif chance == 2:
            pokemon = wizard(author)  
        elif chance == 3:
            pokemon = fighter(author)
        await ctx.send(await pokemon.info()) 
        image_url = await pokemon.show_img()
        if image_url:
            embed = discord.Embed()
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Gagal menampilkan gambar Pokémon.")
    else:
        await ctx.send("Kamu berhasil mendapatkan Pokémon!")

@bot.command()
async def attack(ctx):
    target = ctx.message.mentions[0] if ctx.message.mentions else None  # Mendapatkan pengguna yang disebutkan dalam pesan
    if target:  # Memeriksa apakah ada pengguna yang disebutkan
        # Memeriksa apakah yang diserang dan yang bertahan memiliki Pokémon 
        if target.name in Pokemon.pokemons and ctx.author.name in Pokemon.pokemons:
            enemy = Pokemon.pokemons[target.name]  # Mendapatkan Pokémon pemain bertahan
            attacker = Pokemon.pokemons[ctx.author.name]  # Mendapatkan Pokémon penyerang 
            result = await attacker.attack(enemy)  # Melakukan serangan dan mendapatkan hasilnya
            await ctx.send(result)  # Mengirimkan hasil serangan
        else:
            await ctx.send("Kedua player harus memiliki Pokémon untuk memulai pertempuran!")  # Mengumumkan bahwa setidaknya salah satu petarung tidak memiliki Pokémon 
    else:
        await ctx.send("Tentukan pengguna yang ingin Kalian serang dengan menyebut mereka.")  # Meminta untuk menyebutkan pengguna untuk menyerang



@bot.command()
async def feed(ctx):
    author = ctx.author.name
    if author in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[author]
        response = await pokemon.feed()
        await ctx.send(response)
    else:
        await ctx.send("Anda tidak memiliki Pokemon")

bot.run(token)  # Menjalankan bot dengan token yang diberikan
