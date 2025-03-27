# Инструкция по сборке образа/окружения для запуска тестов в изолированной среде
FROM python:3.12.0a4-alpine3.17
# Базовый образ: Python 3.12 на основе Alpine Linux.

# Добавление дополнительных репозиториев Alpine Linux (версии 3.10) для установки пакетов.
RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories

# Установка браузера Chromium, Chromedriver (для Selenium) и временных зон (tzdata).
RUN apk update  # Обновление списка доступных пакетов.
RUN apk add --no-cache chromium chromium-chromedriver tzdata

# Установка зависимостей
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
# Загрузка ключа для установки glibc (GNU C Library).
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
# Загрузка пакета glibc.
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk
# Загрузка бинарных файлов glibc.

RUN apk update && \
    apk add openjdk11-jre curl tar && \
    # Установка OpenJDK 11 (для Java), утилит curl и tar.
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    # Загрузка Allure (инструмент для генерации отчетов) версии 2.13.8.
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    # Распаковка архива Allure в директорию /opt/.
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    # Создание символической ссылки, чтобы команда `allure` была доступна в системе.
    rm allure-2.13.8.tgz
    # Удаление архива для очистки.

# Установка рабочей директории внутри контейнера в /usr/workspace.
WORKDIR /usr/workspace

# Копирование файла с зависимостями (requirements.txt) из текущей директории на хосте в контейнер.
COPY ./requirements.txt /usr/workspace

# Установка Python-зависимостей, указанных в requirements.txt.
RUN pip3 install -r requirements.txt && pip3 list

