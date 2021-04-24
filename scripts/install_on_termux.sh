termux-info
pkg upgrade -y
pkg install libjpeg-turbo python micro -y
pip install --upgrade pip wheel setuptools
pip install --upgrade tgcf
tgcf --version
tgcf --help
