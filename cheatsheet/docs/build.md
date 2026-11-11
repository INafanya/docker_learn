# Создание образа из Dockerfile
[Ссылка на курс](https://slurm.io/docker){ .md-button .md-button--primary }

## Собираем образ на основе Dockerfile
```
docker build --file Dockerfile --tag test:1.0 . --file
```
`--tag` c тегом (именем образа) `test` и версией `1.0` 
`.` Точка в конце указывает на текущий контекст.

## Более короткая запись
```
docker build -f Dockerfile -t test:1.0 .
```
Флаг `–file` идентичен `–f`
Также `–tag` идентичен `-t`

## Еще более короткая запись
```
docker build –t test:1.0 .
```
Путь к Dockerfile можно не указывать, если он находится в той же директории и называется Dockerfile.

>Важно! Команда для сборки образа `docker build` станет legacy и в будущих версиях Docker будет выключена. Ей на смену пришла команда `docker buildx build`.

> Тем не менее `docker build` будет вызывать новый сборщик по умолчанию, если не установлена переменная DOCKER_BUILDKIT=0.
