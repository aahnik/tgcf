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

## Running with Docker

Using Docker is a recommended way to run `tgcf`, as it encapsulates all dependencies and ensures a consistent environment.

**Prerequisites:**

- Docker installed on your system. You can download it from [Docker's official website](https://www.docker.com/get-started).

**Steps:**

1.  **Clone the Repository (Optional but Recommended for Custom Builds):**
    If you want to build the image locally, potentially with your own modifications, clone the repository:
    ```bash
    git clone https://github.com/aahnik/tgcf.git
    cd tgcf
    ```

2.  **Prepare Configuration Files:**
    `tgcf` requires configuration files to run. You should create these on your host machine in a directory. For example, you can use the cloned `tgcf` directory or a dedicated folder like `~/tgcf_config`.

    *   **`.env` File:** This file is used for the web UI password and other environment-specific settings.
        Create an `.env` file (e.g., in the `tgcf` directory or your chosen config directory):
        ```env
        PASSWORD=your_very_strong_password_here
        # Optional: If using MongoDB for configuration storage via an environment variable
        # MONGO_CON_STR=mongodb://user:pass@host:port/dbname
        ```
        **Security Advice:**
        - Ensure your `PASSWORD` is strong (more than 16 characters recommended).
        - You can use a password manager to store and autofill this password in your browser.

    *   **`tgcf.config.json` File:** This file holds the core `tgcf` forwarding configurations, Telegram API credentials (API ID, API Hash), bot token (if using a bot), plugin settings, etc.
        - If you have cloned the repository, a default `tgcf.config.json` is present in the root. You can copy and modify this.
        - Alternatively, you can let `tgcf` create a default one on its first run (either locally or in Docker if you initially run without mounting it, then copy it out using `docker cp`).
        - **It is crucial to edit this file** with your actual Telegram `API_ID`, `API_HASH`, and forwarding rules (`forwards` section) before `tgcf` can work.

3.  **Build the Docker Image:**
    Navigate to the root of the `tgcf` repository (where the `Dockerfile` is located) and run:
    ```bash
    docker build -t tgcf-app .
    ```
    (You can use a different tag like `tgcf:latest` if you prefer).

4.  **Run the Docker Container:**
    When running the container, you need to:
    - Map the port for the web UI (default `8501`).
    - Mount your configuration files (`.env` and `tgcf.config.json`) into the container.

    Assuming your `.env` and `tgcf.config.json` are in your current directory (e.g., the root of the cloned repo):
    ```bash
    docker run -d \
        --name tgcf-instance \
        -p 8501:8501 \
        -v "$(pwd)/.env:/app/.env" \
        -v "$(pwd)/tgcf.config.json:/app/tgcf.config.json" \
        tgcf-app
    ```
    Breakdown of the command:
    - `-d`: Runs the container in detached mode (in the background).
    - `--name tgcf-instance`: Assigns a memorable name to your container.
    - `-p 8501:8501`: Maps port `8501` on your host to port `8501` inside the container (Streamlit's default port).
    - `-v "$(pwd)/.env:/app/.env"`: Mounts your local `.env` file to `/app/.env` inside the container. The `tgcf` application expects it in its working directory (`/app`).
    - `-v "$(pwd)/tgcf.config.json:/app/tgcf.config.json"`: Mounts your local `tgcf.config.json` to `/app/tgcf.config.json` inside the container.
    - `tgcf-app`: The name of the image you built.

    If your configuration files are in a different directory (e.g., `~/tgcf_config`), adjust the paths in the `-v` flags accordingly:
    ```bash
    docker run -d \
        --name tgcf-instance \
        -p 8501:8501 \
        -v "~/tgcf_config/.env:/app/.env" \
        -v "~/tgcf_config/tgcf.config.json:/app/tgcf.config.json" \
        tgcf-app
    ```

5.  **Accessing the Web UI:**
    Once the container is running, open your web browser and navigate to `http://localhost:8501`. You should be prompted for the password you defined in your `.env` file.

6.  **Managing the Container:**
    - **View logs:** `docker logs tgcf-instance` (use `-f` to follow logs)
    - **Stop the container:** `docker stop tgcf-instance`
    - **Start a stopped container:** `docker start tgcf-instance`
    - **Remove the container (when stopped):** `docker rm tgcf-instance`

7.  **Configuration Persistence & Updates:**
    - Since `tgcf.config.json` is mounted as a volume from your host, any changes made to the configuration through the `tgcf` web UI (that are saved to this file) will persist on your host machine.
    - Your `.env` file is read when the container starts. If you change it, you'll typically need to stop and restart the container for the changes to take effect.

8.  **Using Docker Compose (Optional Advanced Setup):**
    For a more declarative and manageable setup, you can use Docker Compose. Create a `docker-compose.yml` file in the root of your project (or your config directory) like this:

    ```yaml
    version: '3.8'
    services:
      tgcf:
        build: . # Assumes docker-compose.yml is in the repo root with Dockerfile
                 # Or use 'image: tgcf-app' if you've already built it
        container_name: tgcf-service
        ports:
          - "8501:8501"
        volumes:
          - ./tgcf.config.json:/app/tgcf.config.json # Mounts from the same directory as docker-compose.yml
          - ./.env:/app/.env                       # Mounts from the same directory as docker-compose.yml
        restart: unless-stopped # Optional: Automatically restarts the container unless manually stopped
    ```
    **To run with Docker Compose:**
    ```bash
    docker-compose up -d
    ```
    **To stop:**
    ```bash
    docker-compose down
    ```
    Make sure your `tgcf.config.json` and `.env` files are in the same directory as your `docker-compose.yml` if using the relative paths `./` as shown above.

This detailed guide should provide users with comprehensive instructions for setting up and running `tgcf` with Docker. The existing wiki link can be removed or updated to point to this section. For now, I will leave the old link as is, and this new section will be more prominent.

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
