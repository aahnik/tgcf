For more info about running tgcf in the background [read this discussion ➥](https://github.com/aahnik/tgcf/discussions/219)

## Create a  service

Step by step guide

**Step 1.**
Create an **executable shell script** to start tgcf from the proper folder. Let's name it `tgcf_start.sh` and put it in your home folder.

```shell
#!/usr/bin/bash

cd /home/aahnik/Desktop/tgcf # the folder in which tgcf is cloned
# dont use ~ in the path, use full expanded absolute path
# the folder must contain the proper .env and tgcf.config.yml files

# tgcf must be installed inside a virtual env (recommended)
# install tgcf using pip or clone the repo and run poetry install

.venv/bin/tgcf live --loud
```

Make the script executable.

```shell
chmod +x tgcf_start.sh
```

**Step 2.**
Create a service. 

Create a file named `tgcf.service` and put the following content into it.

```ini
[Unit]
Description=The ultimate tool to automate custom telegram message forwarding.
After=network.target

[Install]
WantedBy=multi-user.target

[Service]
Type=simple
ExecStart=/home/aahnik/tgcf_start.sh
# use the absolute path of the shell script in your server
Restart=always
RestartSec=5
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=%n

```

**Step 3.**
Install and enable the service.

```shell
sudo mv tgcf.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable tgcf.service
```


## Running via `systemctl`

Now to **start tgcf** using systemctl you can simply do

```shell
sudo systemctl start tgcf
```

You can also **see the status** of the service by running

```shell
sudo systemctl status tgcf
```

To **see the live logs**

```shell
journalctl -f -u tgcf
```

To **stop the service**

```shell
sudo systemctl stop tgcf 
```


