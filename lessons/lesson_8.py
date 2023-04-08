# https://t.me/ealipatovtelegram_bot

import telebot

bot = telebot.TeleBot("6010041191:AAGZVLrkK8MeJ2YVe1cMVk59_BnktnWj9xY")


@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.chat.id, f'Ты написал мне: {message.text}')


bot.infinity_polling()
