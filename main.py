import asyncio
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot.bot_app.register_handlers import register_handlers
from bot.db.sqlite import db_start
from bot.bot_app.app import bot


async def get_username(chat_id: int):
    chat = await bot.get_chat(chat_id=chat_id)
    username = f"@{chat.username}"

    return username

def register_handler(dp: Dispatcher) -> None:
    register_handlers(dp=dp)

async def main() -> None:
    db_start()

    storage = MemoryStorage()

    dp = Dispatcher(bot, storage=storage)

    register_handler(dp=dp)

    try:
        await dp.start_polling()
    except Exception as _ex:
        pass


if __name__ == "__main__":
    asyncio.run(main())
