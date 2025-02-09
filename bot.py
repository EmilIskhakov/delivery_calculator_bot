import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

API_TOKEN = '7668930405:AAHKKrLILpoQ5x8h9TW0Ttou2KCikqxEOD8'
WEBAPP_HOST = '0.0.0.0'  # IP-адрес сервера
WEBAPP_PORT = int(os.getenv('PORT', 8080))  # Порт, указанный в Render.com
WEBHOOK_PATH = f"/webhook/{API_TOKEN}"  # Путь для вебхука
BASE_URL = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}"  # URL вашего сервера

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть форму",
            web_app=types.WebAppInfo(url="https://delivery-calculator-1.onrender.com")
        )]
    ])
    await message.reply("Нажмите кнопку, чтобы открыть форму:", reply_markup=keyboard)

async def on_startup(app):
    webhook_url = BASE_URL + WEBHOOK_PATH
    await bot.set_webhook(url=webhook_url)

async def on_shutdown(app):
    await bot.delete_webhook()

async def main():
    app = web.Application()
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, WEBAPP_HOST, WEBAPP_PORT)
    await site.start()

if __name__ == '__main__':
    asyncio.run(main())
