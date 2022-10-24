
In Telegram, there are two types of accounts: Users and Bots. With `tgcf` you may use your own user account or a bot that you have created.

<details>
<summary> Read this if you are planning to use a bot account   </summary>
<br>

- You can create a bot from [@BotFather](https://telegram.me/BotFather)
- The bot must be added to the groups and channels (both source and destination)
- The privacy mode of bots should be set to off. That means the bot should be allowed to listen to all messages in the channels/groups it is a member of. By default this setting is `on`, you have to turn privacy mode `off` from BotFather.

</details>

## Default behavior 

When you run `tgcf` for the first time, it will interactively prompt you to enter your phone number or bot token. A session file will be generated and saved in the folder from which you ran `tgcf`.

When you will run `tgcf` again, from the same folder, you will not be required to log in.

## Generate Session String


### Run Online

Click on the below button to run in a free repl. 

[![run on repl](https://docs.replit.com/images/repls/run-on-replit.svg)](https://replit.com/@aahnik/tg-login)

- The session string will not be printed on the screen. (for security purposes)
- The session string will be securely saved in your Saved Messages (if you log in with your own user account).
- The session string will be sent to you (if you log in with a bot account).
- All sensitive user input in the repl is made invisible to ensure high security.

### Run on your machine

- Open your terminal in Mac/Windows/Linux/Android
- Make sure you have `python` installed.
  If you don't have python:
    - for Linux/Mac, its generally already installed.
    - for windows install python 3.8 or above from the Microsoft store
    - for android (termux) run `pkg install python`

- Install `tg-login` by running `pip install tg-login`
- Run `tg-login`
- It will prompt you to enter your details, and then print your session string on the screen.
- Copy the session string, and never share it with anyone.


