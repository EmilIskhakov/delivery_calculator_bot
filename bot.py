import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

API_TOKEN = ''

# Инициализация бота и хранилища состояний
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)  # Создаем диспетчер

# Удаление webhook (если он был установлен)
async def delete_webhook():
    await bot.delete_webhook()

# Создание кнопки для открытия веб-приложения
@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть форму",
            web_app=types.WebAppInfo(url="https://emiliskhakov.github.io/delivery_calculator/index.html")  # Замените на ваш URL
        )]
    ])
    await message.reply("Нажмите кнопку, чтобы открыть форму:", reply_markup=keyboard)

# Запуск бота
async def main():
    # Удаляем webhook, если он активен
    await delete_webhook()
    
    # Запускаем polling
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
