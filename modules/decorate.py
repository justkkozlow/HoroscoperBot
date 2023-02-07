from datetime import datetime
import emoji

current_date = datetime.now().strftime('%d.%m.%Y')
today_message = f'Здравствуйте, гороскоп для всех знаков зодиака на {current_date}:'

choose_signs = "Выберите свой знак зодиака"
sign_description = f"Гороскоп на {current_date}: "


#Zodiacs list
aries = emoji.emojize(':Aries: Овен')
taurus = emoji.emojize(':Taurus: Телец')
gemini = emoji.emojize(':Gemini: Близнецы')
cancer = emoji.emojize(':Cancer: Рак')
leo = emoji.emojize(':Leo: Лев')
virgo = emoji.emojize(':Virgo: Дева')
libra = emoji.emojize(':Libra: Весы')
scorpio = emoji.emojize(':Scorpio: Скорпион')
sagittarius = emoji.emojize(':Sagittarius: Стрелец')
capricorn = emoji.emojize(':Capricorn: Козерог')
aquarius = emoji.emojize(':Aquarius: Водолей')
pisces = emoji.emojize(':Pisces: Рыбы')