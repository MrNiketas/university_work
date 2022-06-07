import logging
from aiogram import Bot, Dispatcher, executor, types

from db import Database

TOKEN = '1781209581:AAGDvr4__ynvn-6IusOSpyTM0jxT__Ug8fg'

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

db = Database('accountant.db')

@dp.message_handler(commands=['start'], content_types='text')
async def start_command(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Привет! У тебя ещё нет анкеты, давай это исправим!")
        await bot.send_message(message.from_user.id, "Как тебя зовут?")
    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегестрированы.")
    await bot.regi
    if message.text == 'конец':
        await bot.send_message(message.from_user.id, "мне конец")



@dp.message_handler(commands=['delete_profile'])
async def delete_command(message: types.Message):
    if (not db.user_exists(message.from_user.id)):
        await bot.send_message(message.from_user.id, "У вас нет профиля.")
    else:
        db.delete_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Ваш профиль успешно удален.")







if __name__ == '__main__':
    executor.start_polling(dp)