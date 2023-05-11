from aiogram import types
from loader import dp, info_all_stoks, bot, db
from aiogram.utils.markdown import hbold


@dp.message_handler(text=info_all_stoks.keys())
async def bot_echo(message: types.Message):
    if db.user_exists(message.from_user.id):
        item = info_all_stoks[message.text]
        text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Название акции: ')} {item.get('Название акции')}\n" \
               f"{hbold('Стоимость акции: ')} {item.get('Стоимость акции')}\n" \
               f"{hbold('Изменение стоимости: ')} {item.get('Изменение стоимости')}\n" \
               f"{hbold('Время информации: ')} {item.get('Время информации')}\n" \
               f"{hbold('Потенциал через год: ')} {item.get('Потенциал через год')}\n" \
               f"{hbold('Капитализация компании: ')} {item.get('Капитализация компании')}\n" \
               f"{hbold('P/E: ')} {item.get('P/E')}\n" \
               f"{hbold('EBITDA: ')} {item.get('EBITDA')}\n" \
               f"{hbold('Дата следующей отчётности: ')} {item.get('Дата следующей отчётности')}\n" \
               f"{hbold('Дивидендный доход: ')} {item.get('Дивидендный доход')}"
        await message.answer(text)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.callback_query_handler(text=info_all_stoks.keys())
async def bot_echo(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        item = info_all_stoks[callback_query.data]
        text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Название акции: ')} {item.get('Название акции')}\n" \
               f"{hbold('Стоимость акции: ')} {item.get('Стоимость акции')}\n" \
               f"{hbold('Изменение стоимости: ')} {item.get('Изменение стоимости')}\n" \
               f"{hbold('Время информации: ')} {item.get('Время информации')}\n" \
               f"{hbold('Потенциал через год: ')} {item.get('Потенциал через год')}\n" \
               f"{hbold('Капитализация компании: ')} {item.get('Капитализация компании')}\n" \
               f"{hbold('P/E: ')} {item.get('P/E')}\n" \
               f"{hbold('EBITDA: ')} {item.get('EBITDA')}\n" \
               f"{hbold('Дата следующей отчётности: ')} {item.get('Дата следующей отчётности')}\n" \
               f"{hbold('Дивидендный доход: ')} {item.get('Дивидендный доход')}"
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

