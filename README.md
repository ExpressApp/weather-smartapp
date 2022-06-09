# Weather SmartApp

С помощью Weather SmartApp ты можешь посмотреть погоду в любом городе мира.

## Установка

1. Воспользуйтесь инструкцией [Руководство администратора](https://express.ms/admin_guide.pdf)
`-> Эксплуатация корпоративного сервера -> Управление контактами -> Чат-боты`
2. Создайте бота в панели администратора eXpress.
3. Получите `secret_key` (Секретный ключ) и `bot_id` (ID) нажав на имя созданного бота.
4. Получите `cts_host` в строке браузера, когда вы в панели администратора.
5. На том же экране установите галку "Включено" и заполните имя SmartApp.


6. Скачайте репозиторий на сервер:

```bash
git clone https://github.com/ExpressApp/weather-smartapp /opt/express/bots/weather-smartapp
cd /opt/express/bots/weather-smartapp
```

7. Получить `weather_secret_key` можно здесь: [weatherapi](<https://www.weatherapi.com/>)


8. Заполните переменные окружения в `docker-compose.yml` реальными значениями:

```
- BOT_CREDENTIALS=cts_host@secret_key@bot_id
- WEATHER_SECRET_KEY=weather_secret_key
```


9. Запустите контейнеры командой:

```bash
docker-compose up -d
```

10. Убедитесь, что в логах нет ошибок.

```bash
docker-compose logs
```

11. Выберите текущий SmartApp через меню SmartApp, проверьте что он открылся.
