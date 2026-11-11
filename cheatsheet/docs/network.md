# Сети в Docker

[Ссылка на курс](https://slurm.io/docker){ .md-button .md-button--primary }

## None
Самый безопасный тип сети. Контейнер не подключается к сети и становится недоступен.
```
docker run –rm -d --network none nginx
```
## Bridge (default)
Если не указывать сеть для подключения, контейнер будет подключён именно к ней
>Docker не поддерживает автоматическое обнаружение служб в сети bridge по умолчанию.

## Host
Убирает сетевую изоляцию между хостом и контейнером.
```
docker run --rm -d --network host nginx
```
## Bridge(User defined)
Docker позволяет создавать пользовательские (свои) сети.
```
docker network create my-slurm-network
docker run --rm -d --network my-slurm-network alpine sleep 100
```

## Ipvlan
## Macvlan
## Overlay