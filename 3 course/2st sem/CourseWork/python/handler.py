import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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
    await message.answer("Введите своё имя",reply_markup=types.ReplyKeyboardRemove())
    await UserProfile.s_name.set()

@dp.message_handler(state=UserProfile.s_name)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["муж", "жен"]
    keyboard.add(*buttons)
    await message.answer("Приятно познакомиться! Теперь назовите ваш пол.",  reply_markup=keyboard)

    await UserProfile.next()

@dp.message_handler(state=UserProfile.s_gender)
async def get_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await message.answer("Отлично! Скажите, сколько вам лет?",reply_markup=types.ReplyKeyboardRemove())
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
    ph = db.get_photo(message.from_user.id)
    caption = output(db.show_profile(message.from_user.id))
    await bot.send_photo(message.from_user.id, ph, caption)

@dp.message_handler(commands=['show_all'])
async def show_all(message: types.Message):
    await bot.send_message(message.from_user.id, db.show_all_profiles(message.from_user.id))

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Зарегестрироваться")
    keyboard.add(button_1)
    await message.answer("Хотите зарегестрироваться??", reply_markup=keyboard)

@dp.message_handler(commands="menu")
async def menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Просмотр анкет")
    button_2 = "Просмотр всех анкет"
    button_3 = "Просмотр профиля"
    button_4 = "Удалить профиль"
    keyboard.add(button_1, button_2, button_3, button_4)
    await message.answer("Жду твоего действия...", reply_markup=keyboard)

@dp.message_handler(commands="q")
async def qw(message: types.Message):
    await message.answer("Напиши мне от какого возраста показывать анкеты?")

@dp.message_handler(commands="q1")
async def qw(message: types.Message):
    await message.answer("Напиши мне до какого возраста показывать анкеты?")

@dp.message_handler(commands="q0")
async def qw(message: types.Message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["муж", "жен"]
    keyboard.add(*buttons)
    await message.answer("Выбери желаемый пол", reply_markup=keyboard)

@dp.message_handler(commands="show")
async def qw(message: types.Message):
    ph = db.get_photo('1100514645')
    caption = output(db.show_profile('1100514645'))
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Написать", callback_data="random_value"))
    await bot.send_photo(message.from_user.id, ph, caption, reply_markup=keyboard)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Дальше", "Стоп"]
    keyboard.add(*buttons)
    await message.answer("Что делаем?", reply_markup=keyboard)

def output(date):
    st = ''
    for item in date:
        if type(item) is int:
            item = str(item)
        st = st + item + '\n'
    return st

if __name__ == '__main__':
    executor.start_polling(dp)