import telebot
from telebot import types

from config import TOKEN
from modules import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def zodiacks_list(message):
    signs_btn = types.InlineKeyboardMarkup(row_width=2)
    for key in sign_list(config.URL):
        btn = types.InlineKeyboardButton(f"{key}", callback_data=f'{key}')
        signs_btn.add(btn)
    bot.send_message(message.chat.id, decorate.choose_signs, reply_markup=signs_btn)


@bot.callback_query_handler(func=lambda call: zodiacks_list)
def sign_content(callback):
    for key in sign_list(config.URL):
        if key == callback.data:
            bot.send_message(callback.message.chat.id, f'{sign_description} {callback.data}')
            bot.send_message(callback.message.chat.id, content(callback))


# def subscribe(answer):
#     subscribe_btn = types.InlineKeyboardMarkup(row_width=2)
#     btn_yes = types.InlineKeyboardButton("Да", callback_data='Yes')
#     btn_no = types.InlineKeyboardButton("Нет", callback_data='No')
#     subscribe_btn.add(btn_yes, btn_no)
#     bot.send_message(answer.chat.id, "Хотите подписаться на уведомления?", reply_markup=subscribe_btn)
#
#
# @bot.callback_query_handler(func= lambda call: subscribe)
# def subscribe_operation(answer):
#     pass


if __name__ == '__main__':
    bot.polling()
