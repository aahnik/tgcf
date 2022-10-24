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
<!-- markdownlint-enable -->

</br>

---
! warning ! this is the readme for version 0.2 (old version), and many information may not be true for present version.
---
---

</br>
Live-syncer, Auto-poster, backup-bot, cloner, chat-forwarder, duplicator, ...

Call it whatever you like! tgcf can fulfill your custom needs.

The *key features* are:

1. Forward messages as "forwarded" or
send a copy of the messages from source to destination chats.

    > A chat can be anything: a group, channel, person or even another bot.

2. Supports two [modes](https://github.com/aahnik/tgcf/wiki/Past-vs-Live-modes-explained)
of operation _past_ or _live_.

    > The past mode deals with all existing messages,
    > while the live mode is for upcoming ones.

3. You may [login](https://github.com/aahnik/tgcf/wiki/Login-with-a-bot-or-user-account)
with a _bot_ or an _user_ account.

    > Telegram imposes certain
    [limitations](https://github.com/aahnik/tgcf/wiki/Using-bot-accounts#limitations)
    on bot accounts.
    You may use an user account to perform the forwards if you wish.

4. Perform custom manipulation on messages.

    > You can
    [filter](https://github.com/aahnik/tgcf/wiki/How-to-use-filters-%3F),
    [format](https://github.com/aahnik/tgcf/wiki/Format-text-before-sending-to-destination),
    [replace](https://github.com/aahnik/tgcf/wiki/Text-Replacement-feature-explained),
    [watermark](https://github.com/aahnik/tgcf/wiki/How-to-use--watermarking-%3F),
    [ocr](https://github.com/aahnik/tgcf/wiki/You-can-do-OCR)
    and do whatever else you need !

5. Detailed [wiki](https://github.com/aahnik/tgcf/wiki) +
Video tutorial.
    > You can also [get help](#getting-help) from the community.

6. If you are a python developer, writing
[plugins](https://github.com/aahnik/tgcf/wiki/How-to-write-a-plugin-for-tgcf-%3F)
for tgcf is like stealing candy from a baby.
    > Plugins modify the message before they are sent to the destination chat.

What are you waiting for? Star the repo and click Watch to recieve updates.

<!-- markdownlint-disable -->
## Video Tutorial

A youtube video is coming soon. [Subscribe](https://www.youtube.com/channel/UCcEbN0d8iLTB6ZWBE_IDugg) to get notified.

<!-- markdownlint-enable -->

## Installation

- If you are an **Windows** user, who is not familiar with the command line, the
[Windows guide](https://github.com/aahnik/tgcf/wiki/Run-tgcf-on-Windows)
is for you.

- To install tgcf on **Android** (Termux), there exists an installer script,
that allows you to install all dependencies by running just a single line command.
Read the
[guide for android](https://github.com/aahnik/tgcf/wiki/Run-on-Android-using-Termux)
to learn.

- If you are familiar with **Docker**, you may read the
[docker guide](https://github.com/aahnik/tgcf/wiki/Install-and-run-using-docker)
for an isolated installation.

- Otherwise for **Linux/Mac**,
    you may install `tgcf` via python's package manager `pip`.

    > **Note:** Make sure you have Python 3.8 or above installed.
    Go to [python.org](https://python.org) to download python.

    Open your terminal and run the following commands.

    ```shell
    pip install --upgrade tgcf
    ```

    To check if the installation succeeded, run

    ```shell
    tgcf --version
    ```

## Usage

Configuring `tgcf` is easy. You just need two files in your present directory
(from which tgcf is invoked).

- [`.env`](https://github.com/aahnik/tgcf/wiki/Environment-Variables)
: To define your environment variables easily.

- [`tgcf.config.yml`](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F)
: An `yaml` file to configure how `tgcf` behaves.

In your terminal, just run `tgcf live` or `tgcf past` to start `tgcf`.
It will prompt you to enter your phone no. or bot token, when you run it
for the first time.

For more details run `tgcf --help` or [read wiki](https://github.com/aahnik/tgcf/wiki/CLI-Usage).

## Deploy to Cloud

Click on [this link](https://m.do.co/c/98b725055148) and get **free 100$**
on Digital Ocean.

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%203.svg)](https://www.digitalocean.com/?refcode=98b725055148&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

> **NOTE** You will get nothing if you directly sign up from Digital Ocean Home Page.
> **Use the link** above, or **click on the big fat button** above to get free 100$.

Deploying to a cloud server is an easier alternative if you cannot install
on your own machine.
Cloud servers are very reliable and great for running `tgcf` in live mode
for a long time.

You can enjoy smooth one-click deploys to the major cloud providers.

- [Heroku](https://github.com/aahnik/tgcf/wiki/Deploy-to-Heroku)
- [Digital Ocean](https://github.com/aahnik/tgcf/wiki/Deploy-to-Digital-Ocean)
- [Gitpod](https://github.com/aahnik/tgcf/wiki/Run-for-free-on-Gitpod")
- [Python Anywhere](https://github.com/aahnik/tgcf/wiki/Run-on-PythonAnywhere)
- [Google Cloud Run](https://github.com/aahnik/tgcf/wiki/Run-on-Google-Cloud)
- [GitHub Actions](https://github.com/aahnik/tgcf/wiki/Run-tgcf-in-past-mode-periodically)

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
