# https://t.me/ealipatovtelegram_bot

import telebot
import lesson_9_game_logic

bot = telebot.TeleBot("6010041191:AAGZVLrkK8MeJ2YVe1cMVk59_BnktnWj9xY")


@bot.message_handler(commands=['start'])
def run_game(message):
    bot.send_message(message.chat.id, f'Игра крестики-нолики началась')
    lesson_9_game_logic.print_game_field()
    current_player = "X"
    while lesson_9_game_logic.check_win():
        if lesson_9_game_logic.check_empty_symbols() != 0:
            lesson_9_game_logic.player_turn(current_player)
            lesson_9_game_logic.check_win()
        else:
            print("Ничья")
            break
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    print("Игра окончена.")


bot.infinity_polling()
