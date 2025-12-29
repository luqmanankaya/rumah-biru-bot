import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

WELCOME_TEXT = """
👋 *Selamat datang ke Rumah Biru (VIP)*

🔹 *Kenapa Rumah Biru?*
Rumah Biru diwujudkan sebagai ruang *education & market reading*  
untuk trader yang mahu memahami pergerakan pasaran dengan lebih jelas.

Fokus utama Rumah Biru:
• Market structure  
• Zone price reaction  
• Pemahaman konteks pasaran  
• Pendidikan trading jangka panjang  

🔵 *Channel Public Rumah Biru*
👉 https://t.me/RUMAHBIRU_PUBLIC

⚠️ *PENTING (Pematuhan & Disclaimer)*
• Semua perkongsian adalah untuk *pendidikan & analisis pasaran sahaja*
• Kami TIDAK memberi arahan BUY / SELL
• Tiada jaminan keuntungan
• Keputusan trading adalah tanggungjawab individu sepenuhnya
• Kandungan ini bukan nasihat pelaburan dan tidak bertujuan melanggar
  mana-mana peraturan Suruhanjaya Sekuriti Malaysia (SC)

👇 Gunakan butang di bawah untuk teruskan
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏠 Kelebihan Private Group", callback_data="kelebihan")],
        [InlineKeyboardButton("🔐 Setup Akses", callback_data="setup")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        WELCOME_TEXT,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "kelebihan":
        await query.edit_message_text(
            "🏠 *Kelebihan Rumah Biru (VIP)*\n\n"
            "• Zone yang kuat & jelas\n"
            "• Education market reading advance\n"
            "• Fokus faham market, bukan signal\n"
            "• Sesuai untuk trader yang nak berdikari\n",
            parse_mode="Markdown"
        )

    elif query.data == "setup":
        await query.edit_message_text(
            "🔐 *Setup Akses Rumah Biru*\n\n"
            "Untuk akses Private Group:\n"
            "1️⃣ Join channel public dahulu\n"
            "2️⃣ Hubungi admin\n"
            "3️⃣ Ikut langkah yang diberikan\n\n"
            "👉 https://t.me/RUMAHBIRU_PUBLIC",
            parse_mode="Markdown"
        )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
