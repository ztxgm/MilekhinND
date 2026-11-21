# Лабораторная работа 6: Введение в FastAPI

## №1 Подготовительный этап
Создание проекта, настройка uv, первый коммит.

![1-1](screenshots/1-1.png)
![1-2](screenshots/1-2.png)
![1-3](screenshots/1-3.png)
![1-4](screenshots/1-4.png)
![1-5](screenshots/1-5.png)
![1-6](screenshots/1-6.png)

## №2 Эндпоинт с параметрами пути и query
Добавление `/items/{item_id}` и тестирование.

![2-1](screenshots/2-1.png)
![2-2](screenshots/2-2.png)
![2-3](screenshots/2-3.png)

## №3 Модель Pydantic и POST-запрос
Создание модели `Item` и эндпоинта `POST /items/`.

![3-1](screenshots/3-1.png)
![3-2](screenshots/3-2.png)
![3-3](screenshots/3-3.png)

## №4 Организация кода (Роутеры)
Вынос маршрутов в `app/routers/items.py`.

![4-1](screenshots/4-1.png)
![4-2](screenshots/4-2.png)
![4-3](screenshots/4-3.png)

## №5 Конфигурация через Pydantic Settings
Настройка `.env` и `app/config.py`.

![5-1](screenshots/5-1.png)
![5-2](screenshots/5-2.png)
![5-3](screenshots/5-3.png)

## №6 Обработка ошибок и документация
Добавление `HTTPException`, `Path`, `Query`, `Field` и метаданных.

![6-1](screenshots/6-1.png)
![6-2](screenshots/6-2.png)

## №7 Самостоятельная работа (PUT)
Обновление товара и валидация уникальности имени.

![7-1](screenshots/7-1.png)
![7-2](screenshots/7-2.png)

## №8 Самостоятельная работа (Логирование)
Добавление логирования.

![8-1](screenshots/8-1.png)
![8-2](screenshots/8-2.png)
