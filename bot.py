from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# IMPORTANT: jangan hardcode token kalau repo public.
# Nanti kita letak token dekat Railway "Variables".
BOT_TOKEN = None

WELCOME_TEXT = """
👋 Selamat datang ke *Rumah Biru (VIP)*

Ini adalah ruang *education & market reading*.
Fokus kami:
• Market structure
• Zone price reaction
• Education advance (BUKAN signal)

❌ Tiada signal BUY/SELL
❌ Tiada jaminan profit
✅ Trader buat keputusan sendiri
"""

PUBLIC_CHANNEL_URL = "https://t.me/RUMAHBIRU_PUBLIC"   # <-- tukar
ADMIN_URL = "https://t.me/RumahBiruAdmin"            # <-- tukar

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔵 Join Channel Public", url=PUBLIC_CHANNEL_URL)],
        [InlineKeyboardButton("📘 Cara Group Berfungsi", callback_data="fungsi")],
        [InlineKeyboardButton("⚙️ Setup Platform", callback_data="setup")],
        [InlineKeyboardButton("👤 Hubungi Admin", url=ADMIN_URL)]
    ]
    await update.message.reply_text(
        WELCOME_TEXT,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.data == "fungsi":
        text = (
            "📘 *Cara Rumah Biru (VIP) berfungsi*\n\n"
            "• Kami kongsi market structure & zone price reaction\n"
            "• Zone = *POTENSI* reaksi, bukan arahan trade\n"
            "• Entry/SL/TP ikut confirmation & risk masing-masing\n\n"
            "Taip /start untuk kembali ke menu."
        )
    elif q.data == "setup":
        text = (
            "⚙️ *Setup Platform*\n\n"
            "Kami bantu dari segi technical setup sahaja.\n"
            "❌ Bukan signal\n"
            "❌ Tiada jaminan profit\n\n"
            "Jika nak dibantu, tekan butang *Hubungi Admin* di menu /start."
        )
    else:
        text = "Taip /start untuk kembali ke menu."

    await q.edit_message_text(text=text, parse_mode="Markdown")

def main():
    import os
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN env var belum set. Set dekat Railway Variables.")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(on_button))

    app.run_polling()

if __name__ == "__main__":
    main()
