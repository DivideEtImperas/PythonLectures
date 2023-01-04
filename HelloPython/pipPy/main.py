from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *




app = ApplicationBuilder().token("5905974673:AAFaBJ6rMh7L7Sx6k2XmRPtA77In6oDLQ6I").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server start')
app.run_polling()





# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))


# from progress.bar import Bar
# import time
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()


# from isOdd import isOdd

# print(isOdd(1)) 
# print(isOdd(4)) 