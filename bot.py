import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
import os

API_TOKEN = '7668930405:AAHKKrLILpoQ5x8h9TW0Ttou2KCikqxEOD8'

# Инициализация бота и хранилища состояний
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)  # Создаем диспетчер

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [  # Единственный ряд с одной кнопкой
            InlineKeyboardButton(
                text="Открыть форму",
                web_app=types.WebAppInfo(url="https://delivery-calculator-1.onrender.com")  # URL веб-приложения
            )
        ]
    ])
    
    await message.reply("Нажмите кнопку, чтобы открыть форму:", reply_markup=keyboard)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
