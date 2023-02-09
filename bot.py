import telebot
from telebot import types

from config import TOKEN
from modules import *

bot = telebot.TeleBot(TOKEN)


@bot.callback_query_handler(func=lambda call: zodiacks_list)
def sign_content(callback):
    for key in sign_list(URL):
        if key == callback.data:
            bot.send_message(callback.message.chat.id,
                             f'{sign_description}\n{callback.data}\n{content(callback)}')

    subscribe_keyboard = types.ReplyKeyboardMarkup(True)
    subscribe_keyboard.row("Да", "Нет")
    bot.send_message(callback.message.chat.id,
                     f'{callback.message.chat.first_name} {subscribe_question}',
                     reply_markup=subscribe_keyboard
                     )


@bot.message_handler(commands=['start'])
def zodiacks_list(message):
    signs_btn = types.InlineKeyboardMarkup(row_width=2)
    for key in sign_list(URL):
        btn = types.InlineKeyboardButton(f"{key}", callback_data=f'{key}')
        signs_btn.add(btn)
    bot.send_message(message.chat.id,
                     f'{message.chat.first_name} {decorate.choose_signs}',
                     reply_markup=signs_btn
                     )


@bot.message_handler(content_types=['text'])
def subscribe(message):
    menu1 = telebot.types.InlineKeyboardMarkup()
    menu1.add(telebot.types.InlineKeyboardButton(text='Первая кнопка', callback_data='first'))
    menu1.add(telebot.types.InlineKeyboardButton(text='Вторая кнопка', callback_data='second'))

    if message.text == 'Да':
        bot.send_message(message.chat.id, text='Нажми первую inline кнопку', reply_markup=menu1)
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, text='До свидания')
        bot.stop_polling()


if __name__ == '__main__':
    bot.polling(none_stop=True)
