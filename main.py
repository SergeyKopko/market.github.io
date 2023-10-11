import telebot
from telebot import types

bot = telebot.TeleBot('6401812078:AAH18KgvxBx8Y54n91RZ53bEYNtsVev46Bw')

@bot.message_handler(commands=['start'])
def main_shop(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    webAppTest = types.WebAppInfo("https://telegram.mihailgok.ru")
    one_butt = types.InlineKeyboardButton(text="Магазин", web_app=webAppTest)
    keyboard.add(one_butt)
    bot.send_message(message.chat.id, 'Добро пожаловать в СНГ магазин по продаже оригинальных кроссовок!', reply_markup=keyboard)


bot.infinity_polling(none_stop=True, interval=0)
