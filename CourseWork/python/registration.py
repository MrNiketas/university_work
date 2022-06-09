import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from db import Database

TOKEN = '1781209581:AAGDvr4__ynvn-6IusOSpyTM0jxT__Ug8fg'

bot = Bot(token = TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

db = Database('accountant.db')

# РЕГЕСТРАЦИЯ
class UserProfile(StatesGroup):
    s_name = State()
    s_gender = State()
    s_age = State()
    s_city = State()
    s_photo = State()
    s_about = State()

@dp.message_handler(commands=['reg'])
async def user_register(message: types.Message):
    await message.answer("Введите своё имя")
    await UserProfile.s_name.set()

@dp.message_handler(state=UserProfile.s_name)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Приятно познакомиться! Теперь назовите ваш пол.")
    await UserProfile.next()

@dp.message_handler(state=UserProfile.s_gender)
async def get_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await message.answer("Отлично! Скажите, сколько вам лет?")
    await UserProfile.next()

@dp.message_handler(state=UserProfile.s_age)
async def get_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Выглядите моложе! В каком городе находитесь?")
    await UserProfile.next()

@dp.message_handler(state=UserProfile.s_city)
async def get_city(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer("Прекрасное место! Отправьте ваше фото.")
    await UserProfile.next()

@dp.message_handler(state=UserProfile.s_photo, content_types=['photo'])
async def get_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    #await message.photo[-1].download('test.jpg')
    await message.answer("Расскажите немного о себе")
    await UserProfile.next()

@dp.message_handler(state=UserProfile.s_about)
async def get_about(message: types.Message, state: FSMContext):
    await state.update_data(about_me=message.text)
    await message.answer("Вы зарегестрированы!")
    buff = await state.get_data()
    db.add_user(message.from_user.id, buff['name'], buff['gender'], buff['age'], buff['city'],
                buff['photo'], buff['about_me'])
    await state.finish()
"""""
@dp.message_handler(commands=['start'], content_types='text')
async def start_command(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        await bot.send_message(message.from_user.id, "Привет! У тебя ещё нет анкеты, давай это исправим!")

    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегестрированы.")
"""""
@dp.message_handler(commands=['delete_profile'])
async def delete_command(message: types.Message):
    if (not db.user_exists(message.from_user.id)):
        await bot.send_message(message.from_user.id, "У вас нет профиля.")
    else:
        db.delete_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Ваш профиль успешно удален.")

@dp.message_handler(commands=['show_my_profile'])
async def show_profile(message: types.Message):
    await bot.send_message(message.from_user.id, db.show_profile(message.from_user.id))

@dp.message_handler(commands=['show_all'])
async def show_all(message: types.Message):
    await bot.send_message(message.from_user.id, db.show_all_profiles(message.from_user.id))

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="/reg")
    keyboard.add(button_1)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp)