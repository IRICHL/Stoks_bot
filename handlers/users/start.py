from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from filters.private_chat import IsPrivate
from loader import dp, db
from re import compile


@dp.message_handler(CommandStart(deep_link=compile(r"\d\d\d")), IsPrivate())
async def bot_start_deeplink(message: types.Message):
    if not db.user_exists(message.from_user.id):
        await message.answer(text=f'Привет, {message.from_user.full_name}!\n'
                                  f'Вы не являетесь подписчиком данного бота.\n'
                                  f'Что бы использовать функции бота, необходимо приобрести подписку.\n',
                             reply_markup=InlineKeyboardMarkup(row_width=1,
                                                               inline_keyboard=[
                                                                   [
                                                                       InlineKeyboardButton(
                                                                           text="Приобрести подписку 500 руб/мес.",
                                                                           callback_data="Подписка"
                                                                       )
                                                                   ]
                                                               ]))
    else:
        await message.answer("Вы уже являетесь подписчиком бота!")


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start_deeplink(message: types.Message):
    if not db.user_exists(message.from_user.id):
        await message.answer(text=f'Привет, {message.from_user.full_name}!\n'
                                  f'Вы не являетесь подписчиком данного бота.\n'
                                  f'Что бы использовать функции бота, необходимо приобрести подписку.\n',
                             reply_markup=InlineKeyboardMarkup(row_width=1,
                                                               inline_keyboard=[
                                                                   [
                                                                       InlineKeyboardButton(
                                                                           text="Приобрести подписку",
                                                                           callback_data="Подписка"
                                                                       )
                                                                   ]
                                                               ]))
    else:
        await message.answer("Вы уже являетесь подписчиком бота!")
