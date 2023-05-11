from aiogram import types
from filters.private_chat import IsPrivate
from keyboards.default import menu
from loader import dp

from data.config import admin_id


@dp.message_handler(IsPrivate(), text="secret", user_id=admin_id)
async def admin_chat_secret(message: types.Message):
    await message.answer("Это секретное сообщение, вызванное админом в лс", reply_markup=menu)
