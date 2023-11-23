# Используйте официальный образ Python
FROM python:3.8

# Установите рабочую директорию
WORKDIR /app

# Скопируйте зависимости и код
COPY requirements.txt .
COPY app.py .

# Установите зависимости
RUN pip install -r requirements.txt

# Укажите команду для запуска приложения
CMD ["python", "app.py"]