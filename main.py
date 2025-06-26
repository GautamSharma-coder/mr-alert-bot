import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [[InlineKeyboardButton("Join Channel", url="https://t.me/YourChannel")]]
    await update.message.reply_text(
        "👋 Welcome to *MR. ALERT*!\n\nUse /alerts, /notes, /test to get started.",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode='Markdown'
    )

async def alerts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📢 *Latest Alerts:*\n- Exam form opens July 10", parse_mode='Markdown')

async def notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📚 *Notes:*\nMaths: [Click](https://link)\nPhysics: [Click](https://link)", parse_mode='Markdown')

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_poll(
        question="🧠 What is 2 + 2?",
        options=["2", "4", "22"],
        correct_option_id=1,
        is_anonymous=False
    )

async def motivate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💡 Don't watch the clock; do what it does. Keep going.")

async def reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏰ Reminder set!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
🛠 *MR. ALERT Commands:*
/start - Start using MR. ALERT
/alerts - View latest alerts
/notes - Get study resources
/test - Take a quiz
/motivate - Daily motivation
/reminder - Set a reminder
/help - Show help menu
""", parse_mode='Markdown')

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("alerts", alerts))
app.add_handler(CommandHandler("notes", notes))
app.add_handler(CommandHandler("test", test))
app.add_handler(CommandHandler("motivate", motivate))
app.add_handler(CommandHandler("reminder", reminder))
app.add_handler(CommandHandler("help", help_command))

app.run_polling()
