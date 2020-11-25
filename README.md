# telegram-chat-sync
A simple code to sync Telegram Chats. Forward the message of one chat to another. May be used for channel sync. ( same message accross channels ); uses Telethon.

## Signing in

First of all you need to have your Account's api_id and api_hash. Read [How to sign in ?](https://docs.telethon.dev/en/latest/basic/signing-in.html)

## Installation

- Install the latest version of [Telethon](https://docs.telethon.dev/en/latest/basic/installation.html)

- Then clone this repo and get started.

## Setup

- Fill up the `config.ini` file with the details.

>Note: The `from` and `to` in the config, must be visibe names and not the user name.

What is the difference between visible name and user name ?

![image](https://user-images.githubusercontent.com/66209958/100173400-7252f480-2ef0-11eb-993a-0ff8a3ddaac1.png)

## Execution

After setting up the `config.ini`, run the `forward.py` script.

You have to login for the first time using your phone number and login code. 

A session file called `forward_sync.session` will be generated. Please don't delete this and make sure to keep this file secret.

To sync another pair of chats, copy the folder with the session file, and then just tweak the `config.ini`, 
with a different source and destination for forwarding.

**Feel free to ask your questions in [![telegram-chat](https://img.shields.io/badge/chat-@aahnikdaw-blue?logo=telegram)](https://telegram.me/aahnikdaw)**
