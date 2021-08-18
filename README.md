# Weather smartapp

Структура проекта

```
.
├── app
│   ├── api        - реализация роутов для приложения, включая необходимые для бота
│   ├── bot        - определение хандлеров, хелперов и тд для бота
│   ├── core       - конфиги, ивенты, общие для приложения сущности
│   ├── db         - модели, функции для работы с бд и миграции
│   ├── resources  - текстовые или файловые ресурсы бота
│   ├── schemas    - сериализаторы
│   ├── services   - сервисы с логикой
│   └── main.py    - запуск сервера с инициализацией необходимых сервисов
├── scripts        - скрипты для запуска тестов, форматеров, линтеров
├── tests          - тесты (внезапно!), структура которых соответствует структуре проекта 
├── pyproject.toml - конфигурация  проекта с зависимостями, версией проекта и его авторами
└── smartapp_files - сборка frontend части
```

## Get Started

* Установить зависимости проекта c помощью менеджера [poetry](https://python-poetry.org/) `poetry install` 
* Определяем переменные окружения в файле `.env`. Пример см. в `example.env`
* Пишем новые команды с помощью [pybotx](https://github.com/ExpressApp/pybotx). 
   Все команды бота находятся `app.bot.commands` и 
   группируются в отдельные модули в зависимости от их логики. 
   Весь текст выносится в `resources.strings`
* Импортируем их в `app.bot.bot` и добавляем в инстанс бота
* Запускаем бд в фоне через [docker-compose](https://docs.docker.com/compose/)

    ```bash
    $ docker-compose up -d db

    ```
* Накатываем все миграции для инициализации бд 
   с помощью [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
    ```bash
    $ alembic upgrade head

    ```
* Запускаем бота как приложение [FastAPI](https://fastapi.tiangolo.com/tutorial/) 
   через [uvicorn](https://fastapi.tiangolo.com/tutorial/).
   Флаг `--reload` используется только при разработке

    ```bash
    $ uvicorn app.main:app --reload
    ```

* Форматируем код, используя
[autoflake](https://github.com/myint/autoflake),
[isort](https://github.com/timothycrosley/isort)
[black](https://github.com/psf/black)

   ```bash
    $ ./scripts/format
    ```

* Запускаем линтеры, используя
[black](https://github.com/psf/black),
[isort](https://github.com/timothycrosley/isort)
[mypy](https://github.com/python/mypy),
[wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide)
    
    ```bash
    $ ./scripts/lint
    ```

