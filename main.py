# aiogram 2 is used deprecated version
import sqlite3 as sq

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from keyboard import keyboard_start

bot = Bot(token='7347503084:AAHF9VnbwIi8Wj_78iBrIbW_T3FpUV-StKQ')
# responsible for async functions of bot
dp = Dispatcher(bot)


async def on_startup(_):
    global cur, base
    base = sq.connect('main.db')
    cur = base.cursor()
    if base:
        print("DB is online!")
    base.execute(
        'CREATE TABLE IF NOT EXISTS users(ID INTEGER, Datatime REAL, Callback INTEGER, LINK TEXT, PRIMARY KEY("ID" AUTOINCREMENT)) ')
    base.commit()

async def start(message: types.Message):
    await bot.send_message(message.chat.id, f"Hello", reply_markup=keyboard_start)

async def start_keyboard(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    print(callback)


if __name__ == "__main__":
    dp.register_message_handler(start, commands='start')
    dp.register_callback_query_handler(start_keyboard, Text(startswith='start_'))


    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
