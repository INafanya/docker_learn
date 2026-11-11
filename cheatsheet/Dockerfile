# Используем официальный образ MkDocs Material в качестве базового
FROM squidfunk/mkdocs-material

# Устанавливаем рабочую директорию
WORKDIR /docs

# Копируем всё содержимое репозитория в /docs внутри образа
COPY . /docs

# Порт, на котором работает mkdocs serve
EXPOSE 8000