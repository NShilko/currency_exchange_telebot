
# Telegram Bot Currency Exchange

Проектное задание по реализацции бота Телеграм

[Демонстрация бота](https://t.me/exchange_trades_test_bot)
## Возможности

- Конвертация валюты
- Отображение списка доступных валют
- Автоматическое исправление ошибок со стороны пользователя ([fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/))


## Установка

1. Для запуска проекта сохраните папку app.

2. Необходимо установить следующие пакеты:

```bash
  pip install pytelegrambotapi
  pip install fuzzywuzzy
  pip install python-levenshtein
```

3. В файле .../app/config.py указать токен вашего бота (1-я строчка):

```bash
  TOKEN = 'input_your_token_here'
```

4. Для запуска в фоновом режиме можете использовать метод [nohup](https://janakiev.com/blog/python-background/):
```bash
  cd .../app
  nohup python3 main.py
```
## Screenshots

![App Screenshot](https://github.com/NShilko/currency_exchange_telebot/blob/main/screenshot/main.png?raw=true)


## Дополнительно

Курс валют предоставляет сервис: https://exchangerate.host/

