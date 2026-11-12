# Установка

[Ссылка на курс](https://slurm.io/docker){ .md-button .md-button--primary }

## Linux
* Установить Docker можно, запустив скрипт установки из терминала.
```
curl -sSL https://get.docker.com/ | sh
```
Альтернативно можно установить Docker вручную, следуя [инструкции](https://docs.docker.com/engine/install/) на официальном сайте.

## Windows
* Для Windows на данный момент есть два способа установки Docker: WSL и Hyper-V. Способ определяет тип бэкенда для запуска Docker. WSL — это стандартный способ, который использует Linux контейнеризацию. Его мы и будем использовать.

* [Windows контейнеризация](https://learn.microsoft.com/en-us/virtualization/windowscontainers/about/) также используется для некоторых сценариев.

* В общем случае установка — это запуск дистрибутива `.еxe` и следование инструкциям установщика.