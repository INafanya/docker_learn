# Описание задания

Задание на подготовку базы данных к использованию в продуктивном окружении используя Docker.

Есть приложение, которое записывает данные в базу и выводит количество записей.

Сборка и запуск приложения
```
docker build -t write_app .
docker run  --network=host write_app
```
1. Создаем отдельную сеть для приложения.
```
docker network create webnet
```
2. Запускаем Nginx веб сервис с пробросом портов(Bind Mount)
```
docker run -d \
  --name web \
  -p 8080:80 \
  -v $(pwd)/html:/usr/share/nginx/html \
  --network webnet \
  nginx:latest
```
3. Запустим БД Postgres с использованием тома(Volume) db-data
```
docker run -d \
  --name db \
  -e POSTGRES_DB=mydatabase \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=password \
  -v db-data:/var/lib/postgresql/data \
  --network webnet \
  postgres:latest
```
4. Приложение с API нужно собрать в кастомный образ
```
docker build -t my-app:latest ./app
```
5. Запускаем приложение с API
```
docker run -d \
  --name app \
  -p 5000:5000 \
  -e ENV=production \
  --network webnet \
  --link db:db \
  my-app:latest
```

Шаг 2. Отредактируйте данный compose файл, чтобы подготовить его к релизу

Шаг 3. После изменений в предыдущих модулях запустите приложение и убедитесь, что оно работает. Таким образом, мы запустили приложение в одну команду и познакомились с составлением docker-compose.