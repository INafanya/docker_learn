# Используем официальный базовый образ с DockerHub
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения в образ
COPY app.py /app/

# Устанавливаем Flask
RUN pip install Flask psycopg2-binary

# Документируем порт 5000
EXPOSE 5000

# Задаем команду для запуска приложения
CMD ["python", "app.py"]
