<!-- markdownlint-disable -->

<p align="center">
<a href = "https://github.com/aahnik/tgcf" > <img src = "https://user-images.githubusercontent.com/66209958/115183360-3fa4d500-a0f9-11eb-9c0f-c5ed03a9ae17.png" alt = "tgcf logo"  width=120> </a>
</p>

<h1 align="center"> tgcf </h1>

<p align="center">
The ultimate tool to automate custom telegram message forwarding.
</p>

<p align="center">
<a href="https://github.com/aahnik/tgcf/blob/main/LICENSE"><img src="https://img.shields.io/github/license/aahnik/tgcf" alt="GitHub license"></a>
<a href="https://github.com/aahnik/tgcf/stargazers"><img src="https://img.shields.io/github/stars/aahnik/tgcf?style=social" alt="GitHub stars"></a>
<a href="https://github.com/aahnik/tgcf/issues"><img src="https://img.shields.io/github/issues/aahnik/tgcf" alt="GitHub issues"></a>
<img src="https://img.shields.io/pypi/v/tgcf" alt="PyPI">
<a href="https://twitter.com/intent/tweet?text=Wow:&amp;url=https%3A%2F%2Fgithub.com%2Faahnik%2Ftgcf"><img src="https://img.shields.io/twitter/url?style=social&amp;url=https%3A%2F%2Fgithub.com%2Faahnik%2Ftgcf" alt="Twitter"></a>
</p>
<p align="center">
<a href="https://github.com/aahnik/tgcf/actions/workflows/quality.yml"><img src="https://github.com/aahnik/tgcf/actions/workflows/quality.yml/badge.svg" alt="Code Quality"></a>
</p>

 Live-syncer, Auto-poster, backup-bot, cloner, chat-forwarder, duplicator, ... Call it whatever you like! **tgcf** is an advanced telegram chat forwarding automation tool that can fulfill all your custom needs.


## Features

Extremely easy to get started yet ready for any complex task you throw at it.

- At its simple form, its just a **telegram message forwarder** that forwards your messages from source to destination chats.
- You can choose the mode: **past** for forward all old(existing messages) or **live** for start forwarding from now. You can either use a telegram bot account or an user account.
<br>

  ![image](https://user-images.githubusercontent.com/66209958/209553073-c6ed1b78-ab8c-43d0-b20d-cd30e543bc34.png)

- You can cutomize every detail of the forwarding with the help of plugins: **filter**(blacklist/whitelist), **format**(bold, italics, etc), **replace**(supports regex), **caption**(header/footer). You can even apply watermark to images/videos, or perform optical character recognition (ocr) on images.
<br>

  ![image](https://user-images.githubusercontent.com/66209958/209553374-8a6f9a5a-8095-4ca7-9f7f-acafe61d9932.png)

- tgcf comes with a **web interface** to customize all these options. You may define you **config in json**, and **run tgcf from the CLI** if you wish.

![image](https://user-images.githubusercontent.com/66209958/209554118-c657e361-8ce2-462d-a305-04e44754cbf7.png)
![image](https://user-images.githubusercontent.com/66209958/209554345-1db31eff-7694-47ef-aede-6a77a7cefb83.png)

<!-- - A **bot interface** is under development. Bot interface means a set of commands, buttons, and conversation flows that will allow you to alter config values while tgcf is running in live mode. -->
<!-- - Any body with basic knowledge of python can easily write plugins for tgcf, thus extending its capabilities. -->
- Detailed [**documentation**](https://github.com/aahnik/tgcf/wiki) and [**videos**](https://www.youtube.com/playlist?list=PLSTrsq_DvEgisMG5BLUf97tp2DoAnwCMG) makes it easy for you to configure tgcf and deploy to any platform of your choice.
  The following videos (english) explain everything in great detail.
  - [Feature Overview](https://youtu.be/FclVGY-K70M)
  - [Running on Windows/Mac/Linux](https://youtu.be/5GzHb6J7mc0)
  <!-- - Running on Android -->
  - [Deploy to Digital Ocean Droplet](https://youtu.be/0p0JkJpfTA0)
- Supported environments **Linux**, **Mac**, Windows (Running Ubuntu on top of **WSL-2**), **Android** (Using Termux app) and any platform where running **Docker** containers is supported.
- All these is **free and open source**, with not a single feature behind a paywall. Tgcf serves to be a free alternative to many commercial telegram bots out there. However you may sponsor to accelerate the development of any new feature and get fast support over chat.


## Install and Run

If you want to use tgcf for free, then run on your own desktop or mobile computer.

Make sure you are on a supported environment and have python:3.10 or above, installed.

- Create a directory and move into it.

  ```shell
  mkdir my-tgcf
  cd my-tgcf
  ```

- Create a python virtual environment and activate it.

  ```shell
  python3 -m venv .venv
  source .venv/bin/activate
  ```

- Install tgcf using `pip`

  ```shell
  pip install tgcf
  tgcf --version
  ```

- Set the password for accessing web interface.
  The password is to be set in the `.env` file.

  ```shell
  echo "PASSWORD=hocus pocus qwerty utopia" >> .env
  ```

  Set your own password, instead of whats given above.

  _Security advice_:

  - Please make sure the password has more than 16 characters.
  - You can save your password in any password manager (may be of browser)
    to autofill password everytime.

- Start the web-server.

  ```shell
  tgcf-web
  ```

To run tgcf without the web-ui read about
[tgcf cli](https://github.com/aahnik/tgcf/wiki/CLI-Usage).

If you are planning to use watermarking and ocr features within tgcf,
you need to install `ffmpeg` and `tesseract-ocr` libraries in you system.
[Read more](https://github.com/aahnik/tgcf/wiki/Additional-Requirements).

See also: [How to install and run using docker ?](https://github.com/aahnik/tgcf/wiki/Install-and-run-using-docker)

## Deploy to Cloud

Click on [this link](https://m.do.co/c/98b725055148) and get **free 200$**
on Digital Ocean.

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%203.svg)](https://www.digitalocean.com/?refcode=98b725055148&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

> **NOTE** You will get nothing if you directly sign up from Digital Ocean Home Page.
> **Use the link** above, or **click on the big fat button** above to get free 200$.

Deploying to a cloud server is an easier alternative if you cannot install
on your own machine.
Cloud servers are very reliable and great for running `tgcf` in live mode
for a long time.

Here are some guides for deployment to different cloud providers.

- [Heroku](https://github.com/aahnik/tgcf/wiki/Deploy-to-Heroku)
- [Digital Ocean](https://github.com/aahnik/tgcf/wiki/Deploy-to-Digital-Ocean)
- [Gitpod](https://github.com/aahnik/tgcf/wiki/Run-for-free-on-Gitpod")
- [Python Anywhere](https://github.com/aahnik/tgcf/wiki/Run-on-PythonAnywhere)
- [Google Cloud Run](https://github.com/aahnik/tgcf/wiki/Run-on-Google-Cloud)

## Getting Help

- First of all [read the wiki](https://github.com/aahnik/tgcf/wiki)
  and [watch the videos](https://www.youtube.com/channel/UCcEbN0d8iLTB6ZWBE_IDugg)
  to get started.

- Type your question in GitHub's Search bar on the top left of this page,
  and click "In this repository".
  Go through the issues, discussions and wiki pages that appear in the result.
  Try re-wording your query a few times before you give up.

- If your question does not already exist,
  feel free to ask your questions in the
  [Discussion forum](https://github.com/aahnik/tgcf/discussions/new).
  Please avoid duplicates.

- For reporting bugs or requesting a new feature please use the [issue tracker](https://github.com/aahnik/tgcf/issues/new)
  of the repo.

## Contributing

PRs are most welcome! Read the [contributing guidelines](/.github/CONTRIBUTING.md)
to get started.

If you are not a developer, you may also contribute financially to
incentivise the development of any custom feature you need.
