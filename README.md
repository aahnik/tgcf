# telegram-chat-forward

[![telegram-chat](https://img.shields.io/badge/chat-@aahnikdaw-blue?logo=telegram)](https://telegram.me/aahnikdaw)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://aahnik.github.io/)

A simple script to forward all the messages of one chat (private/group/channel) to another. Made using Telethon. Can be used to back up the contents of a chat to another place.

## Signing in

First of all you need to have your Telegram account's `api_id` and `api_hash`. 
Learn [how to get](https://docs.telethon.dev/en/latest/basic/signing-in.html) them.

## Installation

- Clone this repo and move into it to get started.

```shell
git clone https://github.com/aahnik/telegram-chat-forward.git && cd telegram-chat-forward
```

- Create a virtual environment and install dependencies.

```shell
python3 -m venv venv && . venv/bin/activate
pip3 install -r requirements.txt
```
> Note: For Windows, the process for activating a virtual environment is different, search Google.

## Setup

You must have the `api_id` and `api_hash` as environment variables.
You may simply create a file named `.env` in the project directory and paste the following into it.

```shell
api_id=12345
api_hash=kjfjfk9r9JOIJOIjoijf9wr0w
```

**Replace the above values with the actual values for your telegram account.**

After this you need to create and fill up the `config.ini` file with your forwarding configurations.

## Note

- The `from` and `to` in the config, must be the visible names of the chat and not the user-name. [Click here](https://user-images.githubusercontent.com/66209958/100173400-7252f480-2ef0-11eb-993a-0ff8a3ddaac1.png) to see the difference between the visible name and the user-name of a chat.

- Any line starting with `;` in a `.ini` file, is treated as a comment.

- You may have as many as forwarding pairs as you wish. Make sure to give a unique header to each pair. Follow the syntax shown below.

```ini
[name of forward1]
; in the above line give any name as you wish
; the square brackets around the name should remain
from = whatAz
to = testWha
offset = 0
; the offset will auto-update, keep it zero initially
[another name]
; the name of section must be unique
from = someone
to = another
offset = 0
```

- You you will run the script next time,only new messages in the `from` chat will be forwarded to the `to` chat. That's why its important not to loose the value of `offset`.

> **Advanced** : You may use the `chat id` instead of visible name. To get the `chat id` of a particular chat/group/channel run `get_chat_id.py` and then enter the user-name/phone/link of the chat.

## Execution

After setting up the `config.ini`, run the `forward.py` script.

```shell
python3 forward.py
```

You have to login for the first time using your phone number (inter-national format) and login code.

A session file called `forwarder.session` will be generated. Please don't delete this and make sure to keep this file secret.

Feel free to ask your questions in the issues section of this repo.
