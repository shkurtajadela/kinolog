from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from .states import GeneralStates
from .app import dp , bot
from .keyboards import inline_kb


async def button_click_callback(callback_query:types.CallbackQuery, state:FSMContext):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    await bot.send_message(callback_query.from_user.id, 'you are a user')


def register_main_handlers_user(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(button_click_callback, state=GeneralStates.user)
    