import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Daftar item yang ingin dideteksi
ITEM_PENTING = [
    "basic sprinkler", "advanced sprinkler", "godly sprinkler", "master sprinkler",
    "bug egg", "paradise egg", "rare summer egg", "mythical egg", "pitcher plant"
]

# Channel sumber dari komunitas Grow a Garden
CHANNEL_SUMBER_IDS = [
    1386768422909640764,
    1386768457399275583,
    1386768441406652537,
    1386768593521217556
]

# Channel tujuan (server kamu)
CHANNEL_TUJUAN_ID = 1377187027954438206

@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id in CHANNEL_SUMBER_IDS:
        konten = message.content.lower()
        for item in ITEM_PENTING:
            if item in konten:
                channel_tujuan = bot.get_channel(CHANNEL_TUJUAN_ID)
                if channel_tujuan:
                    await channel_tujuan.send(
                        f"📦 **Item tersedia:** `{item.title()}`!\n📣 Sumber: <#{message.channel.id}>\n🔗 {message.jump_url}"
                    )
                    print(f"[✔] Notif terkirim: {item}")
                break
    await bot.process_commands(message)

    # --- Commands bantu ---
@bot.command(name="halo")
async def halo(ctx):
    await ctx.send("Halo! Aku bot Grow a Garden 🌱 Siap bantu pantau gear favoritmu!")

@bot.command(name="status")
async def status(ctx):
    await ctx.send("✅ Bot aktif dan memantau gear setiap detik!")

@bot.command(name="list_gear")
async def list_gear(ctx):
    daftar = '\n'.join(f"- {item.title()}" for item in ITEM_PENTING)
    await ctx.send(f"📋 Gear yang dipantau:\n{daftar}")

# --- Run bot ---
TOKEN = os.environ.get("MTM5MDA5ODY1OTMyMzkzNjgwOQ.GHtGQ9.LIhDhUrQ8dwRwUgpjb1aPF7gLgB5qAh2i27XNo")
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ DISCORD_TOKEN belum diset di environment variables!")