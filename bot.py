import telebot
from telebot import types

import schedule
import time

from config import TOKEN
from modules import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def zodiacks_list(message):
    signs_btn = types.InlineKeyboardMarkup(row_width=1)
    for key in sign_list(URL):
        btn = types.InlineKeyboardButton(f"{key}", callback_data=f'{key}')
        signs_btn.add(btn)
    bot.send_message(message.chat.id,
                     f'{message.chat.first_name} {decorate.choose_signs}',
                     reply_markup=signs_btn
                     )


@bot.callback_query_handler(func=lambda call: zodiacks_list)
def sign_content(callback):
    global signs
    for key in sign_list(URL):
        if key == callback.data:
            signs = callback.data
            bot.send_message(callback.message.chat.id,
                             f'Гороскоп на {today(callback)}\n{signs}\n{content(callback)}')
            new_content_questions(callback)
    another_date(callback)


def new_content_questions(callback):
    options_btn = types.InlineKeyboardMarkup(row_width=2)
    yes_btn = types.InlineKeyboardButton("Да", callback_data='yes')
    no_btn = types.InlineKeyboardButton("Нет", callback_data='no')
    options_btn.add(yes_btn, no_btn)
    bot.send_message(callback.message.chat.id,
                     f'Хотите посмотреть гороскоп {signs} на другие даты?',
                     reply_markup=options_btn
                     )


def another_date(callback):
    if callback.data == 'yes':
        content_options_btn = types.InlineKeyboardMarkup(row_width=3)
        yesterday_btn = types.InlineKeyboardButton("Вчера", callback_data='yesterday')
        tomorrow_btn = types.InlineKeyboardButton("Завтра", callback_data='tomorrow')
        week_btn = types.InlineKeyboardButton("Неделя", callback_data='week')
        month_btn = types.InlineKeyboardButton("Месяц", callback_data='month')
        year_btn = types.InlineKeyboardButton("Год", callback_data='year')
        content_options_btn.add(yesterday_btn, tomorrow_btn, week_btn, month_btn, year_btn)
        bot.send_message(callback.message.chat.id,
                         f'На какую дату Вы хотите посмотреть гороскоп',
                         reply_markup=content_options_btn
                         )

    if callback.data == 'yesterday':
        bot.send_message(callback.message.chat.id, f'Гороскоп на {yesterday(callback)}')
    if callback.data == 'tomorrow':
        bot.send_message(callback.message.chat.id, f'Гороскоп на {tommorow(callback)}')
    if callback.data == 'week':
        bot.send_message(callback.message.chat.id, f'Гороскоп на неделю')
    if callback.data == 'month':
        bot.send_message(callback.message.chat.id, f'Гороскоп на {month(callback)}')
    if callback.data == 'year':
        bot.send_message(callback.message.chat.id, f'Гороскоп на {year(callback)} год')
    if callback.data == 'no':
        goodbye_bot(callback)


def subscribe(callback):
    subscribe_btns = types.InlineKeyboardMarkup(row_width=3)
    yes_sub_btn = types.InlineKeyboardButton("Да", callback_data='yes')
    no_sub_btn = types.InlineKeyboardButton("Нет", callback_data='no')
    subscribe_btns.add(yes_sub_btn, no_sub_btn)
    bot.send_message(callback.message.chat.id,
                     f'{callback.message.chat.first_name} {subscribe_question}',
                     reply_markup=subscribe_btns
                     )
    if callback.data == 'no':
        goodbye_bot(callback)
    # else:
    #     id_save = open("id.txt", "w", encoding="utf-8").write(f"{callback.message.chat.id}")
    #     bot.send_message(callback.message.chat.id,
    #                      text='Уведомления включены. Для отмены уведомлений введите /unsubscribe')

    # def subs():
    #     bot.send_message(callback.message.chat.id, text='Test')
    #
    # schedule.every(5).seconds.do(subs)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)


def goodbye_bot(callback):
    bot.send_message(callback.message.chat.id, f'До свидания {callback.message.chat.first_name}')
    bot.stop_polling()


if __name__ == '__main__':
    bot.polling(none_stop=True)
