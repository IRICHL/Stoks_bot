from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu, markup_stoks, best, big_capitalization, small_capitalization, losers, most_cheap, \
    most_traded, most_expensive, overestimated, top, top_dividends, underestimated, best_experts
from loader import dp, db


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирете раздел", reply_markup=menu)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лучшие эксперты")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите группу акций", reply_markup=best_experts)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Акции")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите группу акций", reply_markup=markup_stoks)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лучшие акции США")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите топ", reply_markup=best)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лидеры роста")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите топ", reply_markup=top)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лидеры падения")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите топ", reply_markup=losers)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Недооцененные")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите топ", reply_markup=underestimated)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Переоцененные")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите топ", reply_markup=overestimated)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые дешёвые")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите топ", reply_markup=most_cheap)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые дорогие")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите топ", reply_markup=most_expensive)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="С большой капитализацией")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите топ", reply_markup=big_capitalization)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="С малой капитализацией")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите топ", reply_markup=small_capitalization)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Лучшие дивиденды")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите топ", reply_markup=top_dividends)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Самые активные")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Выбирите топ", reply_markup=most_traded)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Назад")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Вы вернулись на обратную вкладку меню", reply_markup=menu)
    else:
        await message.answer("Вы не являетесь подписчиком бота!")


@dp.message_handler(text="Закрыть меню")
async def show_menu(message: types.Message):
    if db.user_exists(message.from_user.id):
        await message.answer(text="Меню закрыто", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Вы не являетесь подписчиком бота!")
