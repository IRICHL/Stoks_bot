from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, db, best0, info_all_stoks, big_capitalization0, losers0, most_cheap0, most_traded0, most_expensive0, \
    overestimated0, small_capitalization0, top0, top_dividends0, underestimated0, \
    best1, big_capitalization1, losers1, most_cheap1, most_traded1, most_expensive1, overestimated1, \
    small_capitalization1, top1, top_dividends1, underestimated1, \
    best2, big_capitalization2, losers2, most_cheap2, most_traded2, most_expensive2, overestimated2, \
    small_capitalization2, top2, top_dividends2, underestimated2, \
    best3, big_capitalization3, losers3, most_cheap3, most_traded3, most_expensive3, overestimated3, \
    small_capitalization3, top3, top_dividends3, underestimated3
from aiogram.utils.markdown import hbold


@dp.message_handler(text="Лучшие акции США 1-25")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in best0:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лучшие акции США 26-50")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in best1:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лучшие акции США 51-75")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in best2:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лучшие акции США 76-100")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in best3:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="С большой капитализацией 1-25")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in big_capitalization0:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="С большой капитализацией 26-50")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in big_capitalization1:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="С большой капитализацией 51-75")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in big_capitalization2:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="С большой капитализацией 76-100")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in big_capitalization3:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лидеры падения 1-25")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in losers0:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лидеры падения 26-50")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in losers1:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лидеры падения 51-75")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in losers2:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лидеры падения 76-100")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in losers3:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лидеры роста 1-25")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in top0:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лидеры роста 26-50")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in top1:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лидеры роста 51-75")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in top2:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лидеры роста 76-100")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in top3:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые дешёвые 1-25")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in most_cheap0:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые дешёвые 26-50")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in most_cheap1:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые дешёвые 51-75")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in most_cheap2:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые дешёвые 76-100")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in most_cheap3:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые дорогие 1-25")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in most_expensive0:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые дорогие 26-50")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in most_expensive1:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые дорогие 51-75")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in most_expensive2:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые дорогие 76-100")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in most_expensive3:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые активные 1-25")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in most_traded0:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые активные 26-50")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in most_traded1:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые активные 51-75")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in most_traded2:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые активные 76-100")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in most_traded3:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Недооцененные 1-25")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in underestimated0:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Недооцененные 26-50")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in underestimated1:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Недооцененные 51-75")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in underestimated2:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Недооцененные 76-100")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in underestimated3:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Переоцененные 1-25")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in overestimated0:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Переоцененные 26-50")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in overestimated1:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Переоцененные 51-75")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in overestimated2:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Переоцененные 76-100")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in overestimated3:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лучшие дивиденды 1-25")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in top_dividends0:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лучшие дивиденды 26-50")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in top_dividends1:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лучшие дивиденды 51-75")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in top_dividends2:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лучшие дивиденды 76-100")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in top_dividends3:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="С малой капитализацией 1-25")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in small_capitalization0:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="С малой капитализацией 26-50")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in small_capitalization1:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="С малой капитализацией 51-75")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in small_capitalization2:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="С малой капитализацией 76-100")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        for i in small_capitalization3:
            item = info_all_stoks[i]
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
                   f"{hbold('Название акции: ')} {item.get('Название акции')}"
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                              inline_keyboard=[
                                                                                  [
                                                                                      InlineKeyboardButton(
                                                                                          text="Показать данные",
                                                                                          callback_data=item.get('Тикер')
                                                                                      )
                                                                                  ]
                                                                              ]))
    else:
        await message.answer("Вы не являетесь подписчиком бота!")
