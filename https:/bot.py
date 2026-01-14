import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# BOT TOKEN (Railway Variables dan olinadi)
TOKEN = os.getenv("TOKEN")

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom 👋\n\n"
        "Kino kodini yuboring (masalan: 11)\n"
        "Agar kanalga a’zo bo‘lmasangiz, kino berilmaydi."
    )

# Kino kodlarini tekshirish
async def kino_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # MISOL uchun bitta kino
    if text == "11":
        await update.message.reply_text(
            "🎬 Kino nomi: Example Movie\n"
            "🔗 Havola: https://t.me/example_movie"
        )
    else:
        await update.message.reply_text("❌ Bunday kino topilmadi")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHa
