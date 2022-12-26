import telebot

'''Реализовать для телеграм бота:
Напишите программу, удаляющую из текста все слова, содержащие "абв"
'''


def del_abv(text):
    text = text.split(' ')
    return ' '.join([i for i in text if 'абв' not in i])


bot = telebot.TeleBot("5371200500:AAFDNMnE3UtL-TBKwY5vjdayGTn3FI89mGA")



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, del_abv(message.text))


bot.infinity_polling()


