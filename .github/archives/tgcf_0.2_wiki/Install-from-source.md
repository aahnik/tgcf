Warning: This method of installation of `tgcf` is only for python developers, and not recommended for normal users.

## Requirements

| Thing                                        | Why                                                    |
| -------------------------------------------- | ------------------------------------------------------ |
| [`git `](https://git-scm.com/)               | to clone the repo and for version control              |
| [`python`](https://www.python.org/)          | language tgcf is written                               |
| [`poetry`](https://python-poetry.org/)       | used for package management                            |
| [`docker`](https://www.docker.com/)          | if you want to build docker images or run using docker |
| [`make`](https://www.gnu.org/software/make/) | if you are interested in developing                    |




## Steps

1. Clone the repo and move into it
   ```shell
   git clone https://github.com/aahnik/tgcf.git && cd tgcf
   ```

2. Install dependencies with `poetry`
   ```shell
   poetry install
   ```
  > Don't have poetry? Run `pip install pipx` and then `pipx install poetry`. To add poetry to path, run `pipx ensurepath`

3. Activate the virtual environment
   ```shell

   poetry shell
   ```

4. Now the `tgcf` command is available to you.
   ```shell
    tgcf --help
   ```

5. To fetch updates from GitHub
    ```shell
     git fetch && git pull
    ```
    Now, go back to step 2 to install the updates.
