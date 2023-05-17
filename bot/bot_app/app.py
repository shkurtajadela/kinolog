from aiogram import Bot
from dotenv import load_dotenv
import os
from aiogram import Dispatcher


load_dotenv('.env')
token = os.getenv("TOKEN_API")
bot = Bot(token)

dp=Dispatcher(bot)
