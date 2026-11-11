# Загружаем проект на машину
```
git clone https://gitlab.slurm.io/edu/docker_adm_dev_solo.git
```
# Переключаемся на ветку с заданием 
```
git checkout 3.9.practice
```

# Переходим в директорию проекта
```
cd docker_adm_dev_solo/Practice_1
```

# Запускаем сбрке Docker-образа
```
docker build -t slurm-webpage:1.0 .
```

# Запуск Docker-контейнера
```
docker run -d -p 80:80 slurm-webpage:1.0
```