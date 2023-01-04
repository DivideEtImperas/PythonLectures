from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('E:\\Programming\\PythonLectures\\HelloPython\\pipPy\\db.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()