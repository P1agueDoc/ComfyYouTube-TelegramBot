# ComfyYouTube-TelegramBot
It's a bot that allows you to (kinda) watch YouTube from a Telegram chat using a bot


# How to start
- Install necessary dependencies:
  
    pip install -r requirements.txt
  
    install https://github.com/tdlib/telegram-bot-api  (you can follow this guide here: https://tdlib.github.io/telegram-bot-api/build.html?os=Windows)
- Get cookies because YouTube may block downloads:
  
    in firefox - download extension cookies.txt. Go to youtube (you should be logged) and use extension (press on it) to download cookies from youtube OR just download all cookies. in chrome - use any other extension that does the job.
- get your Telegram bot api key from BotFather
- go to https://my.telegram.org/ and get api-id and api-hash
- go to telegram-bot-api folder (not root bot folder) and create a .txt there.
- Open  .txt and write:
  
    cd your-path\telegram-bot-api\bin
  
    telegram-bot-api --local --http-port=8081 --http-ip-address=127.0.0.1 --api-id=your-api-id --api-hash=your-hash
- rename .txt into start.bat
- open start.bat and hide it away
- Go to folder with bot
- Open the file DreamyVideo in a text editor (notepad)
- Fill gaps:
  
    API_URL = "your-api-id" (it should be made like that: http://127.0.0.1:8081/bot[your-bot-api] example: API_URL = "http://127.0.0.1:8081/bot67457850:krpkfL54lg450kg4g
  
    bot = telebot.TeleBot("your-bot-api")
- Save and close
- Open in text editor file named video_download
- Fill gap:
  
    'cookiefile': r"path-to-cookies"
- Save and close
- Create venv opening cmd in this folder and writing: python -m venv .venv
- activate venv in cmd: .\venv\Scripts\activate
- start bot by writing: python3 DreamyVideo.py
- Go into telegram into chat with your bot and press /start to get info
- Enjoy your bot

# Unreadable code or caveman writing
Sorry for bad code. I was really tired while writing it and just wanted to finish it quickly. And i'm still learning python.

# YouTube sending Forbidden 403
Can't really do anything here. create cookies.txt again, it might help for a few hours or days?.


# No continues for you
sorry, this project is no longer worked on
