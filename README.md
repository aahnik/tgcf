# telegram-chat-forward

A simple script to forward all the messages of one chat (private/group/channel) to another. Made using Telethon. Can be used to back up the contents of a chat to another place.

## Signing in

First of all you need to have your Telegram account's `api_id` and `api_hash`. 

Learn [How to sign in ?](https://docs.telethon.dev/en/latest/basic/signing-in.html) using Telethon.

## Installation

- Install the latest version of [Telethon](https://docs.telethon.dev/en/latest/basic/installation.html).

            pip3 install -U telethon cryptg pillow
- You may install some optional dependancies to improve performance.

            sudo apt update && sudo apt install clang lib{jpeg-turbo,webp}-dev python{,-dev} zlib-dev

- Now clone this repo to get started.

             git clone https://github.com/aahnik/telegram-chat-forward.git

## Setup

- Fill up the `config.ini` file with your details.

**Note:** The `from` and `to` in the config, must be the visible names and not the user name.

What is the difference between visible name and user name ?

![image](https://user-images.githubusercontent.com/66209958/100173400-7252f480-2ef0-11eb-993a-0ff8a3ddaac1.png)

## Execution

After setting up the `config.ini`, run the `forward.py` script.

           python3 forward.py

You have to login for the first time using your phone number and login code. 

A session file called `forward_sync.session` will be generated. Please don't delete this and make sure to keep this file secret.


**Feel free to ask your questions in [![telegram-chat](https://img.shields.io/badge/chat-@aahnikdaw-blue?logo=telegram)](https://telegram.me/aahnikdaw)**
