#!/bin/bash
cd $(dirname $0)
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade tgcf
screen -d -m tgcf-web













#sudo docker ps -aq | xargs sudo docker stop | xargs sudo docker rm
#sudo apt install python3 python3-pip
#echo yes | pip3 install -r requirements-cli.txt
#echo yes | pip3 install -r requirements.txt
#cp config_sample.env config.env
#echo yes | sudo docker container prune
#echo yes | sudo docker image prune -a
#sudo dockerd
#sudo docker build . -t tgcf
#sudo docker run -p 8501:8501 tgcf
#docker pull aahnik/tgcf
#sudo docker run -it -p 8501:8501 tgcf
#docker run -d -p 8501:8501 --env-file .env aahnik/tgcf
#docker logs beautiful_mclean
