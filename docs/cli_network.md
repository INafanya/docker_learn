# Команды

[Ссылка на курс](https://slurm.io/docker){ .md-button .md-button--primary }

## docker network ls 
```
docker network ls
```
Показывает все сети.


## docker network connect
```
docker network connect <имя_сети> <имя_или_id_контейнера>
```
Подключает контейнер к сети.
## docker network create 
```
docker network create <имя_сети>
```
Создаёт сеть.
## docker network disconnect 
```
docker network disconnect <имя_сети> <имя_или_id_контейнера>
```
Отключает контейнер от сети.
## docker network inspect 
```
docker network inspect <имя_сети>
```
Показывает больше информации о сети.


## docker network prune
```
docker network prune 
```
Удаляет все неиспользуемые сети.
## docker network rm 
```
docker network rm <имя_сети>
```
Удаляет конкретную сеть.
