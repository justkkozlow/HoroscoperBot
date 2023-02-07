import telebot
from telebot import types

from modules import config, decorate
from modules.config import TOKEN

from modules.get_content import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    signs_btn = types.InlineKeyboardMarkup(row_width=2)
    aries = types.InlineKeyboardButton(f"{decorate.aries}", callback_data='aries')
    taurus = types.InlineKeyboardButton(f"{decorate.taurus}", callback_data='taurus')
    gemini = types.InlineKeyboardButton(f"{decorate.gemini}", callback_data='gemini')
    cancer = types.InlineKeyboardButton(f"{decorate.cancer}", callback_data='cancer')
    leo = types.InlineKeyboardButton(f"{decorate.leo}", callback_data='leo')
    virgo = types.InlineKeyboardButton(f"{decorate.virgo}", callback_data='virgo')
    libra = types.InlineKeyboardButton(f"{decorate.libra}", callback_data='libra')
    scorpio = types.InlineKeyboardButton(f"{decorate.scorpio}", callback_data='scorpio')
    sagittarius = types.InlineKeyboardButton(f"{decorate.sagittarius}", callback_data='sagittarius')
    capricorn = types.InlineKeyboardButton(f"{decorate.capricorn}", callback_data='capricorn')
    aquarius = types.InlineKeyboardButton(f"{decorate.aquarius}", callback_data='aquarius')
    pisces = types.InlineKeyboardButton(f"{decorate.pisces}", callback_data='pisces')
    signs_btn.add(aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces)
    bot.send_message(message.chat.id, decorate.today_message)
    bot.send_message(message.chat.id, start_content(config.URL))
    bot.send_message(message.chat.id, decorate.choose_signs, reply_markup=signs_btn)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(callback):
    for key in sign_list:
        if key == callback.data:
            bot.send_message(callback.message.chat.id, content(callback))


if __name__ == '__main__':
    bot.polling()
