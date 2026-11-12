# Security

[Ссылка на курс](https://slurm.io/docker){ .md-button .md-button--primary }

## Списки уязвимостей Docker
[Mitre](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=docker){ .md-button .md-button--primary }
[Opencve](https://app.opencve.io/cve/?vendor=docker&product=docker&cvss=&search=docker){ .md-button .md-button--primary }


`CVE` (Common Vulnerabilities and Exposures) — общеизвестные уязвимости информационной безопасности.
У каждой уязвимости есть номер CVE-год-номер, подробности и оценка CVSS v3.1 от 0 до 10, чем больше — тем уязвимость опаснее

## Официальная информация от Docker
[Docker Security](https://docs.docker.com/security/security-announcements){ .md-button .md-button--primary }


## Docker bench
Cкрипт, который проверяет десятки общих рекомендаций по развертыванию контейнеров Docker.
```
git clone https://github.com/docker/docker-benchsecurity.git
cd docker-bench-security
docker-compose run --rm docker-bench-security
```

## Clair
Cтатического анализ уязвимостей в контейнерах.
```
git clone https://github.com/quay/clair.git
cd clair
docker-compose up -d
```