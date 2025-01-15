# ComfyYouTube-TelegramBot
It's a bot to watch youtube (kinda) from telegram chat by bot


# How to start
- install all that needed:
  
    pip install -r requirements.txt
  
    install https://github.com/tdlib/telegram-bot-api  (you can use guide here: https://tdlib.github.io/telegram-bot-api/build.html?os=Windows)
- Get cookies because Youtube may block download:
  
    in firefox - download extension coockies.txt. Go to youtube (you should be logged) and use extension (press on it) to download cookies from youtube OR just download all cookies. in chrome - use any other extension that does the job.
- get Telegram bot api from BotFather
- go to https://my.telegram.org/ and get api-id and api-hash
- go to telegram-bot-api folder (not our bot folder) and create a .txt there.
- write into .txt:
  
    cd your-path\telegram-bot-api\bin
  
    telegram-bot-api --local --http-port=8081 --http-ip-address=127.0.0.1 --api-id=your-api-id --api-hash=your-hash
- rename .txt into start.bat
- open start.bat and hide it away
- Go to folder with bot
- Open in text book file named DreamyVideo
- Fill gaps:
  
    API_URL = "your-api-id"
  
    bot = telebot.TeleBot("your-bot-api")
- Save and close
- Open in text book file named video_download
- Fill gap:
  
    'cookiefile': r"path-to-cookies"
- Save and close
- Create venv opening cmd in this folder and writing: python -m venv .venv
- activate venv: .\venv\Scripts\activate
- Go into telegram into chat with your bot and press /start to get info
- Enjoy your bot

# Unreadable code or caveman writing
Sorry for bad code, i just got really tired when writing it and decided to just finish it quickly. And i still learning python.
