from bot.db.db_interface import get_kinolog
from .app import dp, bot
from . import messages
from . keyboards import get_ikb_registration, get_ikb_user_type, get_ikb_kinolog_form, get_ikb_kinolog_card
from aiogram import types, Dispatcher
from .states import GeneralStates
from aiogram.dispatcher import FSMContext


async def send_welcome(message:types.Message):
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)

    welcome_msg = "Привет! Это бот для заполнения анкеты кинологом или поиска кинолога владельцем собаки. \nЕсли хотите зарегистрироваться, то нажимайте кнопку ниже"
    await message.answer(text=welcome_msg, reply_markup=get_ikb_registration())
    await GeneralStates.registration.set()


async def send_help(message:types.Message):
    await message.answer(messages.HELP_MESSAGE)


async def callback_choose_user_type(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'registration':
        await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

        await bot.send_message(chat_id=callback.from_user.id, text="Кто Вы?", reply_markup=get_ikb_user_type())
        await GeneralStates.choose_user.set()


async def callback_load_interface(callback: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

    if callback.data == 'kinolog':
        try:
            kinolog = get_kinolog(callback.from_user.id)
            if kinolog['form_status']=='selected':
                text = 'Это интерфейс одобренного кинолога. \nЧто вы хотите делать дальше:'
                await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=get_ikb_kinolog_card())
                await GeneralStates.kinolog.set()
            else:
                text = "Ваша заявка в ожидании"
                await bot.send_message(chat_id=callback.from_user.id, text=text)
                await GeneralStates.start.set()
        except:
            text = "Это интерфейс кинолога. \nЧто вы хотите делать дальше:"
            await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=get_ikb_kinolog_form())
            await GeneralStates.kinolog.set()
    elif callback.data == 'user':
        text = 'Это интерфейс клиента. \nЧто вы хотите делать дальше:'
        await bot.send_message(chat_id=callback.from_user.id, text=text)
        await GeneralStates.user.set()


def register_main_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(send_welcome, commands=['start'], state='*')
    dp.register_message_handler(send_help, commands=['help'], state='*')
    # dp.register_message_handler(send_registration, state=GeneralStates.registration)
    dp.register_callback_query_handler(callback_choose_user_type, state=GeneralStates.registration)
    dp.register_callback_query_handler(callback_load_interface, state=GeneralStates.choose_user)
    