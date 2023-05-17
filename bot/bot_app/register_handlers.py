from aiogram import Dispatcher
from bot.bot_app.kinolog import register_main_handlers_kinolog
from bot.bot_app.user import register_main_handlers_user
from bot.bot_app.commands import register_main_handlers


def register_handlers(dp: Dispatcher) -> None:
    register_main_handlers_kinolog(dp=dp)
    register_main_handlers(dp=dp)
    register_main_handlers_user(dp=dp)

