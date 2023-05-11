from aiogram import types
from loader import dp, db


@dp.message_handler()
async def bot_echo(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Такого тикера нету")
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


