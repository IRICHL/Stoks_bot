from aiogram import types
from loader import dp, bot,db, info_all_stoks, top_analysts0, top_analysts1, top_analysts2, top_analysts3, top_analysts4, \
    top_analysts5, top_analysts6, top_analysts7, top_analysts8, top_analysts9, top_analysts10, top_analysts11, top_analysts12, \
    top_analysts13, top_analysts14, top_analysts15, top_analysts16, top_analysts17, top_analysts18, top_analysts19, top_analysts20, top_analysts21, top_analysts22, top_analysts23, top_analysts24, \
    top_bloggers0, top_bloggers1, top_bloggers2, top_bloggers3, top_bloggers4, \
    top_bloggers5, top_bloggers6, top_bloggers7, top_bloggers8, top_bloggers9, top_bloggers10, top_bloggers11, top_bloggers12, \
    top_bloggers13, top_bloggers14, top_bloggers15, top_bloggers16, top_bloggers17, top_bloggers18, top_bloggers19, top_bloggers20, top_bloggers21, top_bloggers22, top_bloggers23, top_bloggers24, \
    top_insiders0, top_insiders1, top_insiders2, top_insiders3, top_insiders4, \
    top_insiders5, top_insiders6, top_insiders7, top_insiders8, top_insiders9, top_insiders10, top_insiders11, top_insiders12, \
    top_insiders13, top_insiders14, top_insiders15, top_insiders16, top_insiders17, top_insiders18, top_insiders19, top_insiders20, top_insiders21, top_insiders22, top_insiders23, top_insiders24
from aiogram.utils.markdown import hbold
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.callback_query_handler(text="a0")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts0:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)


@dp.callback_query_handler(text="a1")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts1:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a2")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts2:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a3")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts3:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a4")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts4:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a5")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts5:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a6")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts6:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a7")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts7:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a8")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts8:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a9")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts9:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a10")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts10:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a11")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts11:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a12")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts12:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a13")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts13:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a14")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts14:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a15")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts15:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a16")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts16:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a17")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts17:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a18")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts18:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a19")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts19:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a20")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts20:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a21")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts21:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a22")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts22:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a23")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts23:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="a24")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_analysts24:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b0")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers0:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b1")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers1:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b2")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers2:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b3")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers3:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b4")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers4:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b5")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers5:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b6")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers6:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b7")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers7:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b8")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers8:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b9")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers9:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b10")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers10:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b11")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers11:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b12")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers12:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b13")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers13:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b14")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers14:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b15")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers15:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b16")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers16:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b17")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers17:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b18")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers18:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b19")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers19:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b20")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers20:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b21")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers21:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b22")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers22:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b23")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers23:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="b24")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_bloggers24:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i0")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders0:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i1")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders1:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i2")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders2:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i3")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders3:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i4")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders4:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i5")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders5:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i6")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders6:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i7")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders7:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i8")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders8:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i9")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders9:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i10")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders10:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i11")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders11:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i12")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders12:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i13")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders13:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i14")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders14:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i15")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders15:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i16")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders16:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i17")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders17:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i18")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders18:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i19")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders19:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i20")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders20:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i21")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders21:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i22")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders22:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i23")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders23:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(text="i24")
async def bot_info_analysts(callback_query: types.CallbackQuery):
    if db.user_exists(callback_query.from_user.id):
        for item in top_insiders24:
            text = f"{hbold('Тикер: ')} {item.get('Тикер')}\n" \
               f"{hbold('Рекомендация: ')} {item.get('Рекомендация')}\n" \
               f"{hbold('Дата: ')} {item.get('Дата')}"
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text)
    else:
        text = "Вы не являетесь подписчиком бота."
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text)

