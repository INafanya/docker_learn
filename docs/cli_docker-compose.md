# Команды для работы с Compose

[Ссылка на курс](https://slurm.io/docker){ .md-button .md-button--primary }


>Важно! В старых версиях утилиты команда используется с дефисом: `docker-compose`.
## docker compose config
```
docker compose config
```
Валидирует и выводит конфигурацию docker compose.yaml.
## docker compose up
```
docker compose up
```
Запускает все контейнеры из docker compose.yaml, захватывает терминал для вывода логов).
```
docker compose up -d
```
Запускает приложения в режиме detached, в бэкграунде, не захватывает терминал для вывода логов.
## docker compose down
```
docker compose down
```
Останавливает все контейнеры.
## docker compose ps
```
docker compose ps
```
Показывает все запущенные контейнеры.
## docker compose logs
```
docker compose logs
```
Показывает все логи.
```
docker compose logs <имя_сервиса>
```
Показывает все логи для `определённого` контейнера.
## docker compose restart
```
docker compose restart
```
Перезагружает всё приложение.
```
docker compose restart <имя_сервиса>
```
Перезагружает `определённый` контейнер.
## docker compose exec
```
docker compose exec <имя_сервиса> <команда>
```
Позволяет запустить команду в выбранном контейнере.