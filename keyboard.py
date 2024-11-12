from aiogram import types


def keyboard_start():
    start_keyboard = types.InlineKeyboardMarkup(row_width=1)
    start_b1 = types.InlineKeyboardButton(text='Some text', callback_data="start_start")
    start_b2= types.InlineKeyboardButton(text='AI support', callback_data="start_AI")
    start_b3 = types.InlineKeyboardButton(text="Day schedule", callback_data="start_schedule")
    start_keyboard.add(start_b1, start_b2, start_b3)
    return start_keyboard


keyboard_start = keyboard_start()
