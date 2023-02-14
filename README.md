# GameSong

## The Team
- Ran Elbaz
- Jonik Shafir
- Idan Teperovich

## About this bot

This is a Telegram bot implemented in Python programming language. The bot has various functions, including playing a guessing game, changing settings, and displaying help information. The bot is interactive and uses inline keyboards to present options to the user. When the user chooses to play the game

![after press start](https://user-images.githubusercontent.com/117281221/218689638-22d80a74-8a8e-400a-8810-812cbc2f4362.png)

the bot selects a random song and sends lyrics to the user one by one. The user has to guess the name of the song. If the user guesses correctly, the bot sends a success message; otherwise, the game ends after a set number of attempts, and the bot sends a failure message. The bot also allows the user to change the language and theme of the game.

LINK TO THE BOT: https://t.me/GameSongsBot

🚧 ADD SCREENSHOTS/GIFS/SCREENCAST HERE (REFER TO MARKDOWN'S SYNTAX FOR HELP ON DISPLAYING IMAGES)

🚧 ADD ANY OTHER NOTES REGARDING THE BOT
 
## Instructions for Developers 
### Prerequisites
- Python 3.10
- Poetry
- 🚧 ADD ANY OTHER PREREQUISITE HERE (MONGODB?)

### Setup
- git clone this repository 
- cd into the project directory
- Install dependencies:
    
      poetry install


- Get an API Token for a bot via the [BotFather](https://telegram.me/BotFather)
- Create a `bot_settings.py` file with your bot token:

      BOT_TOKEN = 'xxxxxxx'

### Running the bot        
- Run the bot:

      poetry run python bot.py
