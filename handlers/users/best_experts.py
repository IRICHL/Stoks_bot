from aiogram import types
from loader import dp, top_bloggers, top_analysts, top_insiders, db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hbold


@dp.message_handler(text="25 лучших аналитиков")
async def bloggers(message: types.Message):
    if db.user_exists(message.from_user.id):
        i = 0
        for item in top_analysts:
            text = f"{hbold('Имя: ')} {item}\n" \
                   f"{hbold('Компания: ')} {top_analysts[item].get('Компания')}\n" \
                   f"{hbold('Доходность: ')} {top_analysts[item].get('Доходность')}\n" \
                   f"{hbold('Индекс успеха: ')} {top_analysts[item].get('Индекс успеха')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать рекомендации",
                                                                                          callback_data=f"a{i}"
                                                                                      )
                                                                                  ]
                                                                              ]))
            i += 1
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="25 лучших финансовых блогеров")
async def bloggers(message: types.Message):
    if db.user_exists(message.from_user.id):
        i = 0
        for item in top_bloggers:
            text = f"{hbold('Имя: ')} {item}\n" \
                   f"{hbold('Компания: ')} {top_bloggers[item].get('Компания')}\n" \
                   f"{hbold('Доходность: ')} {top_bloggers[item].get('Доходность')}\n" \
                   f"{hbold('Индекс успеха: ')} {top_bloggers[item].get('Индекс успеха')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать рекомендации",
                                                                                          callback_data=f"b{i}"
                                                                                      )
                                                                                  ]
                                                                              ]))
            i += 1
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="25 лучших инсайдеров")
async def bloggers(message: types.Message):
    if db.user_exists(message.from_user.id):
        i = 0
        for item in top_insiders:
            text = f"{hbold('Имя: ')} {item}\n" \
                   f"{hbold('Компания: ')} {top_insiders[item].get('Компания')}\n" \
                   f"{hbold('Доходность: ')} {top_insiders[item].get('Доходность')}\n" \
                   f"{hbold('Индекс успеха: ')} {top_insiders[item].get('Индекс успеха')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать рекомендации",
                                                                                          callback_data=f"i{i}"
                                                                                      )
                                                                                  ]
                                                                              ]))
            i += 1
    else:
        await message.answer("Вы не являетесь подписчиком бота!")
