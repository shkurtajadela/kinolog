from .app import dp, bot
from . import messages
from . keyboards import inline_kb
from aiogram import types, Dispatcher
from .states import GeneralStates
from aiogram.dispatcher import FSMContext


async def send_welcome(message:types.Message):
    await message.answer(messages.WELCOME_MESSAGE)


async def send_help(message:types.Message):
    await message.answer(messages.HELP_MESSAGE)


async def send_registration(message:types.Message):
    await message.answer(messages.REGISTRATION_MESSAGE, reply_markup=inline_kb)
    await GeneralStates.choose_user.set()


async def callback_user_type(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'kinolog':
        text = 'Welcome to kinolog interface! If you are a new kinolog, go to /form or \n/selected!'
        await bot.send_message(chat_id=callback.from_user.id, text=text)
        await GeneralStates.kinolog.set()
    elif callback.data == 'user':
        text = 'Welcome to user interface! Go to /dogform to write information about your dog!'
        await bot.send_message(chat_id=callback.from_user.id, text=text)
        await GeneralStates.user.set()


def register_main_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(send_welcome, commands=['start'], state='*')
    dp.register_message_handler(send_help, commands=['help'], state='*')
    dp.register_message_handler(send_registration, commands=['registration'], state='*')
    dp.register_callback_query_handler(callback_user_type, state=GeneralStates.choose_user)
    