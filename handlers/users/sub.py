from loader import dp, db, bot
from data.config import yootoken
from aiogram import types
from aiogram.types.message import ContentType
import time
from inc import days_to_seconds


@dp.callback_query_handler(text="Подписка")
async def sub(callback_query: types.CallbackQuery):
    if not db.user_exists(callback_query.from_user.id):
        await bot.send_invoice(chat_id=callback_query.from_user.id, title="Оформление подписки", description="Подписка на прогнозы и информацию об акциях", payload="month_sub", provider_token=yootoken, currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб", "amount": 50000}])


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
    if message.successful_payment.invoice_payload == "month_sub":
        # Подписываем пользователя
        time_sub = int(time.time()) + days_to_seconds(30)
        db.add_user(message.from_user.id)
        db.set_time_sub(message.from_user.id, time_sub)
        await bot.send_message(message.from_user.id, text="Вам выдана подписка на месяц!")
