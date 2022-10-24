It is assumed that you are familiar with basic `docker` commands. Docker should be properly installed and running in your system. 


- Make sure you have understood how `tgcf` is run by passing certain variables via [command-line options](https://github.com/aahnik/tgcf/wiki/CLI-usage) or by setting them as [environment variables](https://github.com/aahnik/tgcf/wiki/Environment-Variables).
- Read about [`tgcf.config.yml`](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F) to know how you can configure `tgcf`

## Install


Pull the [official docker image](https://hub.docker.com/r/aahnik/tgcf) from DockerHub.

```shell
docker pull aahnik/tgcf
```

> **Tip**: Use `aahnik/tgcf:minimal` for a smaller image size. (beta)

## Configure

- Write all your [environment variables](https://github.com/aahnik/tgcf/wiki/Environment-Variables#create-a-env-file) in a file called `.env`.
- Write your [configuration](https://github.com/aahnik/tgcf/wiki/How-to-configure-tgcf-%3F)
 in `tgcf.config.yml`.

## Run

```shell
docker run -v absolute/path/to/tgcf.config.yml:/app/tgcf.config.yml -d --env-file .env aahnik/tgcf
```

Note:
- the `-d` flag tells the docker command to run the container in detached mode.
- the `--env-file` option passes the file `.env` for its variables to be used inside the container.


## Check

To see if your container is running,

```shell
$ docker ps
CONTAINER ID   IMAGE               COMMAND       CREATED          STATUS          PORTS     NAMES
ae4d7d6651ca   aahnik/tgcf       "tgcf --loud"   3 minutes ago    Up 3 minutes              zen_gates

```

The container id and name will be different in your machine.

To see the logs produced by the container,

```shell
$ docker logs zen_gates
```

Replace `zen_gates` with the name of the container in your machine.



