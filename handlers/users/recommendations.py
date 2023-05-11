from aiogram import types
from loader import dp, bot, info_all_stoks,db
from aiogram.utils.markdown import hbold


@dp.callback_query_handler(text=info_all_stoks.keys())
async def bot_echo(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        item = info_all_stoks[callback_query.data]
        text = f"{hbold('Тикер: ')} {item.get('Тикер')}"
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)
