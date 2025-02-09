import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

API_TOKEN = '7668930405:AAHKKrLILpoQ5x8h9TW0Ttou2KCikqxEOD8'

# Получаем порт из переменных окружения (Render.com)
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT', 8080))

# URL для вебхука
BASE_URL = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}"  # Внешний URL вашего сервиса
WEBHOOK_PATH = f"/webhook/{API_TOKEN}"
WEBHOOK_URL = BASE_URL + WEBHOOK_PATH

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть форму",
            web_app=types.WebAppInfo(url="https://delivery-calculator-1.onrender.com")  # URL веб-приложения
        )]
    ])
    await message.reply("Нажмите кнопку, чтобы открыть форму:", reply_markup=keyboard)

# Настройка вебхука при старте
async def on_startup(app):
    await bot.set_webhook(url=WEBHOOK_URL)

# Очистка вебхука при остановке
async def on_shutdown(app):
    await bot.delete_webhook()

# Главная функция для запуска бота
async def main():
    app = web.Application()
    
    # Регистрация обработчика вебхука
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    
    # Добавление событий старта и остановки
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    
    # Запуск сервера
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, WEBAPP_HOST, WEBAPP_PORT)
    await site.start()

    # Бесконечный цикл для поддержания работы
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
