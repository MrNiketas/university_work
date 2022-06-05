import logging
from aiogram import Bot, Dispatcher, executor, types

from db import Database

TOKEN = '1781209581:AAGDvr4__ynvn-6IusOSpyTM0jxT__Ug8fg'

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

db = Database('accountant.db')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите ваше Имя")
    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегестрированы")
"""""
@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        db.
"""""




if __name__ == '__main__':
    executor.start_polling(dp)