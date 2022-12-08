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

Live-syncer, Auto-poster, backup-bot, cloner, chat-forwarder, duplicator, ...

Call it whatever you like! tgcf can fulfill your custom needs.

## Videos

<!-- markdownlint-enable -->

The following videos (english) explain everything in great detail.

- [Feature Overview](https://youtu.be/FclVGY-K70M)
- [Running on Windows/Mac/Linux](https://youtu.be/5GzHb6J7mc0)
- Running on Android
- [Deploy to Digital Ocean Droplet](https://youtu.be/0p0JkJpfTA0)

## Supported environments

- Linux
- Mac
- Windows (Running Ubuntu on top of WSL-2)
- Android (Using Termux app)
- Any Linux VPS

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
