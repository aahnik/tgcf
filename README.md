<!-- markdownlint-disable -->

<p align="center">
<a href = "https://github.com/aahnik/tgcf" > <img src = "https://user-images.githubusercontent.com/66209958/115183360-3fa4d500-a0f9-11eb-9c0f-c5ed03a9ae17.png" alt = "tgcf logo"  width=120> </a>
</p>

<h1 align="center"> tgcf </h1>

<p align="center">
The ultimate tool to automate telegram message forwarding.
</p>

<p align="center"><a href="https://github.com/aahnik/tgcf/blob/main/LICENSE"><img src="https://img.shields.io/github/license/aahnik/tgcf" alt="GitHub license"></a>
<a href="https://github.com/aahnik/tgcf/stargazers"><img src="https://img.shields.io/github/stars/aahnik/tgcf?style=social" alt="GitHub stars"></a>
<a href="https://github.com/aahnik/tgcf/issues"><img src="https://img.shields.io/github/issues/aahnik/tgcf" alt="GitHub issues"></a>
<img src="https://img.shields.io/pypi/v/tgcf" alt="PyPI">
<a href="https://twitter.com/intent/tweet?text=Wow:&amp;url=https%3A%2F%2Fgithub.com%2Faahnik%2Ftgcf"><img src="https://img.shields.io/twitter/url?style=social&amp;url=https%3A%2F%2Fgithub.com%2Faahnik%2Ftgcf" alt="Twitter"></a></p>

<br>

<!-- markdownlint-enable -->

The *key features* are:

1. Two [modes of operation](https://github.com/aahnik/tgcf/wiki/Past-vs-Live-modes-explained)
are _past_ or _live_ for dealing with either existing or upcoming messages.
2. Supports [signing in](https://github.com/aahnik/tgcf/wiki/Signing-in-with-a-bot-or-user-account)
with both telegram _bot_ account as well as _user_ account.
3. Custom [Filtering](https://github.com/aahnik/tgcf/wiki/How-to-use-filters-%3F)
of messages based on whitelist or blacklist.
4. Modification of messages like [Text Replacement](https://github.com/aahnik/tgcf/wiki/Text-Replacement-feature-explained),
[Watermarking](https://github.com/aahnik/tgcf/wiki/How-to-use--watermarking-%3F),
[OCR](https://github.com/aahnik/tgcf/wiki/You-can-do-OCR-!) etc.
5. Detailed **[documentation📖](https://github.com/aahnik/tgcf/wiki)** +
Video tutorial + Fast help in [discussion forum💬](https://github.com/aahnik/tgcf/discussions).
6. If you are a python developer, writing [plugins🔌](https://github.com/aahnik/tgcf/wiki/How-to-write-a-plugin-for-tgcf-%3F)
is like stealing candy from a baby.

What are you waiting for? Star 🌟 the repo and click Watch 🕵 to recieve updates.

You can also join the official [Telegram Channel](https://telegram.me/tg_cf),
to recieve updates without any ads.

<!-- markdownlint-disable -->
## Video Tutorial 📺

A youtube video is coming soon. [Subscribe](https://www.youtube.com/channel/UCcEbN0d8iLTB6ZWBE_IDugg) to get notified.

<!-- markdownlint-enable -->

## Run Locally 🔥

> **Note:** Make sure you have Python 3.8 or above installed.
Go to [python.org](https://python.org) to download python.

| Platform | Supported |
| -------- | :-------: |
| Windows  |     ✅     |
| Mac      |     ✅     |
| Linux    |     ✅     |
| [Android](https://github.com/aahnik/tgcf/wiki/Run-on-Android-using-Termux)  |     ✅     |

If you are familiar with **Docker**, you may [go that way](https://github.com/aahnik/tgcf/wiki/Install-and-run-using-docker)
for an easier life.

Open your terminal (command prompt) and run the following commands.

```shell
pip install tgcf
```

To check if the installation succeeded, run

```shell
tgcf --version
```

If you see an error, that means installation failed.

### Configuration 🛠️

Configuring `tgcf` is easy. You just need two files in your present directory
(from which tgcf is invoked).

- [`.env`](https://github.com/aahnik/tgcf/wiki/Environment-Variables) : To
define your environment variables easily.

- [`tgcf.config.yml`](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F) :
An `yaml` file to configure how `tgcf` behaves.

### Start `tgcf` ✨

In your terminal, just run `tgcf live` or `tgcf past` to start `tgcf`.

For more details run `tgcf --help` or [read docs](https://github.com/aahnik/tgcf/wiki/CLI-Usage).

## Run on cloud 🌩️

Deploying to a cloud server is an easier alternative if you cannot install
on your own machine.
Cloud servers are very reliable and great for running `tgcf` in live mode.

When you are deploying on a cloud platform, you can configure `tgcf`
using [environment variables](https://github.com/aahnik/tgcf/wiki/Environment-Variables).
The contents of [`tgcf.config.yml`](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F)
can be put inside the environment variable called `TGCF_CONFIG`.

You may click on the platform name *(left coloumn)* to learn more about the
deployment process. Clicking on the "deploy" button *(right coloumn)* will
directly deploy the application to that platform.

<!-- markdownlint-disable -->

<br>

| Platform                                                     |                       One click deploy                       |
| ------------------------------------------------------------ | :----------------------------------------------------------: |
| [Heroku](https://github.com/aahnik/tgcf/wiki/Deploy-to-Heroku) | <a href="https://heroku.com/deploy?template=https://github.com/aahnik/tgcf">   <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" width=155></a> |
| [Digital Ocean](https://github.com/aahnik/tgcf/wiki/Deploy-to-Digital-Ocean) | <a href="https://cloud.digitalocean.com/apps/new?repo=https://github.com/aahnik/tgcf/tree/main">  <img src="https://www.deploytodo.com/do-btn-blue.svg" alt="Deploy to DO" width=220></a> |
| [Google Cloud](https://github.com/aahnik/tgcf/wiki/Run-on-Google-Cloud) | <a href="https://deploy.cloud.run/?git_repo=https://github.com/aahnik/tgcf.git"> <img src="https://deploy.cloud.run/button.svg" alt="Run on Google Cloud" width=210></a> |
| [Gitpod](https://github.com/aahnik/tgcf/wiki/Run-for-free-on-Gitpod) | <a href="https://gitpod.io/#https://github.com/aahnik/tgcf">  <img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Run on Gitpod" width=160></a> |

<br>
<!-- markdownlint-enable -->

If you need to run `tgcf` in past mode periodically, then you may set a cron job
in your computer or  use [GitHub Actions](https://github.com/aahnik/tgcf/wiki/Run-tgcf-in-past-mode-periodically)
to run a scheduled workflow.

## Getting Help 💁🏻

- First of all [read the wiki](https://github.com/aahnik/tgcf/wiki)
and [watch](https://www.youtube.com/channel/UCcEbN0d8iLTB6ZWBE_IDugg) the videos.
- If you still have doubts, you can try searching your problem in discussion
forum or the issue tracker.
- Feel free to ask your questions in the [Discussion forum](https://github.com/aahnik/tgcf/discussions/new).
- For reporting bugs or requesting a feature please use the [issue tracker](https://github.com/aahnik/tgcf/issues/new)
for this repo.

Please do not send me direct messages on Telegram.
(Exception: Sponsors can message me anytime)
