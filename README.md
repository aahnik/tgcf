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

The *key features* are:

1. Two [modes of operation](https://github.com/aahnik/tgcf/wiki/Past-vs-Live-modes-explained) are _past_ or _live_ for dealing with either existing or upcoming messages.
2. Supports [signing in](https://github.com/aahnik/tgcf/wiki/Signing-in-with-a-bot-or-user-account) with both telegram _bot_ account as well as _user_ account.
3. Custom [Filtering](https://github.com/aahnik/tgcf/wiki/How-to-use-filters-%3F) of messages based on whitelist or blacklist.
4. Modification of messages like [Text Replacement](https://github.com/aahnik/tgcf/wiki/Text-Replacement-feature-explained), [Watermarking](https://github.com/aahnik/tgcf/wiki/How-to-use--watermarking-%3F), [OCR](https://github.com/aahnik/tgcf/wiki/You-can-do-OCR-!) etc.
5. Detailed **[documentation📖](https://github.com/aahnik/tgcf/wiki)** + Video tutorial + Fast help in [discussion forum💬](https://github.com/aahnik/tgcf/discussions).
6. If you are a python developer, writing [plugins🔌](https://github.com/aahnik/tgcf/wiki/How-to-write-a-plugin-for-tgcf-%3F) is like stealing candy from a baby.

What are you waiting for? Star 🌟 the repo and click Watch 🕵 to recieve updates.

You can also join the official [Telegram Channel](https://telegram.me/tg_cf), to recieve updates without any ads.

## Video Tutorial 📺

A youtube video is coming soon. [Subscribe](https://www.youtube.com/channel/UCcEbN0d8iLTB6ZWBE_IDugg) to get notified.

## Local Installation 🔥

This guide is for installing and running on your own computer (Windows/Mac/Linux/Android).

> **Note:** Make sure you have Python 3.8 or above installed. Go to [python.org](https://python.org) to download python.

Open your terminal (command prompt) and run the following commands.

```shell
pip install pipx
pipx install tgcf
```

To check if the installation succeeded, run

```shell
tgcf --version
```

If you see an error, that means installation failed.


## Supported Platforms 🌩️

Deploying to a cloud server is an easier alternative if you cannot install on your own machine. Cloud servers are very reliable and great for running `tgcf` in live mode.

| Platform                  | Supported Modes | How to ?                                                     | Minimum Price |
| ------------------------- | --------------- | ------------------------------------------------------------ | ------------- |
| Heroku                    | live            | <a href="https://heroku.com/deploy">   <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy"></a> | Free          |
| GitHub Actions            | past            | ![](https://user-images.githubusercontent.com/66209958/115380652-6b56b680-a1f0-11eb-8eff-eda079b33120.png) | Free          |
| Digital Ocean             | past + live     | <a href="https://cloud.digitalocean.com/apps/new?repo=https://github.com/{repo-owner}/{repo-name}/tree/{branch-name}">  <img src="https://www.deploytodo.com/do-btn-blue.svg" alt="Deploy to DO" width=220></a> | $5            |
| Gitpod                    | past + live     | <a href="https://cloud.digitalocean.com/apps/new?repo=https://github.com/{repo-owner}/{repo-name}/tree/{branch-name}">  <img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Deploy to DO" width=180></a> | Free          |
| Windows/Mac/LInux/Android | past + live     |  <img src="https://user-images.githubusercontent.com/66209958/115380909-aeb12500-a1f0-11eb-9776-5622c223dc77.png" alt="Deploy to DO" width=180></a>                                                            | Free          |
| Docker                    | past + live     |       <img src="" alt="Deploy to DO" width=200>                             | Free          |
| Google Cloud              | past + live     | <img src="https://deploy.cloud.run/button.svg" alt="Deploy to DO" width=200> | Free          |


## Configuration ⚙️

Configuring `tgcf` is easy. You just need two files.

- [`.env`](https://github.com/aahnik/tgcf/wiki/Environment-Variables) : You heard it right! Just `.env`. This file is for storing your secret credentials for signing into Telegram. This file is for defining the environment variables. You can do so by other methods also.

- [`tgcf.config.yml`](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F) : An `yaml` file to configure how `tgcf` behaves.


## Getting Help 💁🏻

- First of all [read the wiki](https://github.com/aahnik/tgcf/wiki) and [watch the videos.
- If you still have doubts, you can try searching your problem in discussion forum or the issue tracker.
- Feel free to ask your questions in the [Discussion forum](https://github.com/aahnik/tgcf/discussions/new).
- For reporting bugs or requesting a feature please use the [issue tracker](https://github.com/aahnik/tgcf/issues/new) for this repo.

Please do not send me direct messages in Telegram. (Exception: Sponsors can message me anytime)
