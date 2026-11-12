# Аналоги Docker
[Ссылка на курс](https://slurm.io/docker){ .md-button .md-button--primary }

Интерфейс пользовательского пространства для функций взаимодействия с ядром Linux

## Podman
CLI совместим с командами Docker (например, podman run вместо docker run).
```
sudo apt install podman
podman run -d -p 8080:80 nginx
```
## Containerd
Containerd обычно используется в составе более крупных контейнерных платформ (например, Kubernetes), но может работать и независимо.
```
sudo ctr image pull docker.io/library/nginx:latest
sudo ctr run --rm -t docker.io/library/nginx:latest nginx-test
```

## CRI-O
CRI-O сосредоточен на предоставлении облегчённой среды выполнения для Kubernetes, а не на общем управлении контейнерами.
```
sudo apt install cri-o
sudo systemctl start crio
sudo crictl pull nginx
sudo crictl runp nginx