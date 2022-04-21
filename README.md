# Weather SmartApp


## Инструкция по развёртыванию weather-smartapp

1. Воспользуйтесь инструкцией [Руководство
   администратора](https://express.ms/admin_guide.pdf) `-> Эксплуатация корпоративного
   сервера -> Управление контактами -> Чат-боты`, чтобы создать бота в панели
   администратора eXpress.

   Получите `secret_key` и `bot_id` нажав на имя созданного бота.
   Получите `cts_host` в строке браузера, когда вы в панели администратора.

   На том же экране установите галку "SmartApp enabled" и заполните имя
   смартаппа.


2. Скачайте репозиторий на сервер:

```bash
git clone https://github.com/ExpressApp/weather-smartapp /opt/express/bots/weather-smartapp
cd /opt/express/bots/weather-smartapp
```

3. Заполните переменные окружения `BOT_CREDENTIALS` и `WEATHER_SECRET_KEY`
   (<https://www.weatherapi.com/>) в `docker-compose.yml` реальными значениями.


4. Запустите контейнеры командой:

```bash
docker-compose up -d
```

5. Убедитесь, что в логах нет ошибок.

```bash
docker-compose logs
```

6. Выберите текущий SmartApp через меню смартаппов, проверьте что он открылся.
