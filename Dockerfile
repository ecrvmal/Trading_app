# Используем Docker - образ с  python 3.10
FROM python:3.10

# Установка рабочей директории
WORKDIR /app

# Копируем зависимости в контейнер
COPY ./requirements.txt /app/

# Копируем проект в контейнер
COPY ./ /app/

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]