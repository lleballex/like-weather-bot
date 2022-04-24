# ⚡ likeWeatherBot

Telegram bot that gives access to the weather of any city from any country. The data can be viewed 5 days in advance. In the bot there is a setting of the displayed units of measurement, everything can be customized for yourself. **[Start bot](https://t.me/likeWeatherBot)**

### Tools:

- 💪 Aiogram
- 😄 Peewee
- 🤹🏽 PyOWM

## Getting started

### Installing

##### For windows

```bash
git clone https://github.com/lleballex/like-weather-bot.git
cd like-weather-bot
python -m venv env
env\scripts\activate
pip install -r requirements.txt
cd src

# First write the data to .env (more details below)

python bot.py migrate
```

##### For linux

```bash
git clone https://github.com/lleballex/like-weather-bot.git
cd like-weather-bot
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
cd src

# First write the data to .env (more details below)

python bot.py migrate
```

#### like-weather-bot/.env

```
BOT_TOKEN=bot api token (@BotFather)
OWM_TOKEN=owm api token (openweathermap.org)
```

### Starting

```bash
python bot.py
```

## Contact me:

[<img width="30px" title="lleballex | Telegram" src="https://raw.githubusercontent.com/github/explore/main/topics/telegram/telegram.png">](https://t.me/lleballex)
[<img width="30px" title="lleballex | VK" src="https://raw.githubusercontent.com/github/explore/main/topics/vk/vk.png">](https://vk.com/lleballex)
