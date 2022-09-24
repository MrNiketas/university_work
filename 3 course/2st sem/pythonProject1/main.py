import pyTelegramBotApi

from pyTelegramBotApi import types

token="5761808205:AAHOzoT6V-9ZO4pZ7Vecw7HPlqVXiFDZ4gw"
bot=pyTelegramBotApi.TeleBot(token)
@bot.message_handler(commands=["start"])
def ye(message):
    markup=types.ReplayKeyboardMarkup(resize_keyboard=True)
    button1=types.KeyboardButton("Просто кнопка1", replay_markup=markup)
    button2=types.KeyboardButton("Просто кнопка2", replay_markup=markup)
    markup.add(button1,button2)
    bot.send_message(message.chat.id,"Выбери что-нибудь",reply_markup=markup)
bot.polling(none_stop=True)
