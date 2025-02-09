import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
import os

API_TOKEN = '7668930405:AAHKKrLILpoQ5x8h9TW0Ttou2KCikqxEOD8'

# Инициализация бота и хранилища состояний
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)  # Создаем диспетчер

# Настройка главного меню с одной командой /start
async def set_main_menu():
    commands = [
        BotCommand(command="start", description="Начать работу"),  # Команда для старта
    ]
    await bot.set_my_commands(commands)

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть форму",
            web_app=types.WebAppInfo(url="https://delivery-calculator-1.onrender.com")  # URL веб-приложения
        )]
    ])
    await message.reply("Добро пожаловать! Нажмите кнопку, чтобы открыть форму:", reply_markup=keyboard)

# Запуск бота
async def main():
    await set_main_menu()  # Устанавливаем главное меню
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
