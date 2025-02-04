# Используем официальный Python образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы из текущей директории в рабочую директорию контейнера
COPY . .

# Устанавливаем все зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем переменную окружения для токена
ENV BOT_TOKEN="your_telegram_bot_token"

# Запускаем бота
CMD ["python", "bot.py"]
