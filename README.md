# telegram-chat-forward

[![telegram-chat](https://img.shields.io/badge/chat-@aahnikdaw-blue?logo=telegram)](https://telegram.me/aahnikdaw)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://aahnik.github.io/)

A simple script to forward all the messages of one chat (indivisual/group/channel) to another. Made using Telethon. Can be used to back up the contents of a chat to another place.

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

## Configuration

- The `from` and `to` in the `config.ini` has to be a username/phone/link/chat_id of the chat.
- **To confirm that you are using the correct `from` and `to` run the `get_chat_info.py` script.**

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

> **Note**:Any line starting with `;` in a `.ini` file, is treated as a comment.

## Offset

- When you run the script for the first time, keep `offset=0`.
- When the script runs, the value of offset in `config.ini` gets updated automatically.
- Offset is basically the id of the last message forwarded from `from` to `to`.
- When you run the script next time, the messages in `from` having an id greater than offset (newer messages) will be forwarded to  `to`. That is why it is important not to loose the value of `offset`.

## Execution

After setting up the `config.ini`, run the `forwarder.py` script.

```shell
python3 forwarder.py
```

You have to login for the first time using your phone number (inter-national format) and login code.

A session file called `forwarder.session` will be generated. Please don't delete this and make sure to keep this file secret.

Feel free to ask your questions in the [Discussion section](https://github.com/aahnik/telegram-chat-forward/discussions). For bugs and feature requests use the [issues](https://github.com/aahnik/telegram-chat-forward/issues/new) section of this repo.

## Extra

To get all information about any particular chat:

- Run the script `run_chat_info.py`.
- Open Telegram and send `.id` to any chat to get the chat id.
- Send `.info` to any chat to get details of the chat.
- When you are done, come back to your terminal and press <kbd>CTRL</kbd> + <kbd>C</kbd> to stop.
