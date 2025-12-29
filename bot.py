import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

WELCOME_TEXT = """
👋 *Selamat datang ke Rumah Biru (VIP)*

🔷 *Kenapa Rumah Biru?*
Rumah Biru diwujudkan sebagai ruang *education & market reading* untuk trader yang mahu memahami pergerakan pasaran dengan lebih jelas dan berdisiplin.

Fokus utama Rumah Biru:
• Market structure  
• Zone price reaction  
• Pemahaman konteks pasaran  
• Pendidikan trading jangka panjang  

Kami percaya trader yang faham pasaran akan lebih bertanggungjawab dalam membuat keputusan sendiri.

🔵 *Channel Public Rumah Biru*
👉 https://t.me/RUMAHBIRU_PUBLIC

⚠️ *PENTING (Pemantuhan & Disclaimer)*
• Semua perkongsian adalah untuk tujuan *pendidikan & analisis pasaran sahaja*  
• Kami TIDAK memberi arahan BUY / SELL  
• Tiada jaminan keuntungan  
• Keputusan trading adalah tanggungjawab individu sepenuhnya  
• Kandungan ini bukan nasihat pelaburan dan tidak bertujuan melanggar mana-mana peraturan Suruhanjaya Sekuriti Malaysia (SC)

⬇️ Gunakan butang di bawah untuk maklumat lanjut
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔐 Kelebihan Private Group", callback_data="benefit")],
        [InlineKeyboardButton("🛠️ Setup Akses", callback_data="setup")],
        [InlineKeyboardButton("📢 Channel Public", url="https://t.me/RUMAHBIRU_PUBLIC")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        WELCOME_TEXT,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
