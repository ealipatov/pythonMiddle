# https://t.me/ealipatovtelegram_bot

import telebot
import lesson_9_game_logic

bot = telebot.TeleBot("6010041191:AAGZVLrkK8MeJ2YVe1cMVk59_BnktnWj9xY")
current_player = ['X']


@bot.message_handler(commands=['start'])
def run_game(message):
    bot.send_message(message.chat.id, f'Игра крестики-нолики началась')
    bot.send_message(message.chat.id, lesson_9_game_logic.print_game_field())
    bot.send_message(message.chat.id, f'Ходят {current_player[0]}')


@bot.message_handler(content_types=['text'])
def turn(message):
    if lesson_9_game_logic.check_win() == lesson_9_game_logic.game_status:
        if lesson_9_game_logic.check_empty_symbols() != 0:
            bot.send_message(message.chat.id, lesson_9_game_logic.check_input(message.text, current_player[0]))
            bot.send_message(message.chat.id, lesson_9_game_logic.print_game_field())
            bot.send_message(message.chat.id, lesson_9_game_logic.check_win())
        else:
            bot.send_message(message.chat.id, "Ничья")
        if current_player[0] == "X":
            current_player[0] = "O"
        else:
            current_player[0] = "X"
        if lesson_9_game_logic.check_empty_symbols() != 0:
            bot.send_message(message.chat.id, f'Ходят {current_player[0]}')
    else:
        bot.send_message(message.chat.id, "Игра окончена.")


bot.infinity_polling()
