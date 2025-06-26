import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to MR. ALERT!")

async def alerts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📢 Exam form opens July 10!")

async def notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📚 Notes: Maths, Physics, Chemistry")

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_poll(
        question="🧠 What is 2 + 2?",
        options=["2", "4", "22"],
        correct_option_id=1,
        is_anonymous=False
    )

async def motivate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💡 Keep going, you’re doing great!")

async def reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏰ Reminder feature coming soon.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
MR. ALERT Commands:
/start - Start the bot
/alerts - Latest updates
/notes - Study notes
/test - Quiz
/motivate - Motivation
/reminder - Set reminder
/help - Help menu
""")

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("alerts", alerts))
app.add_handler(CommandHandler("notes", notes))
app.add_handler(CommandHandler("test", test))
app.add_handler(CommandHandler("motivate", motivate))
app.add_handler(CommandHandler("reminder", reminder))
app.add_handler(CommandHandler("help", help_command))

app.run_polling()
