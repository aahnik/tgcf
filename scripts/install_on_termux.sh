termux-info
pkg upgrade -o Dpkg::Options::="--force-confnew" --force-yes -y
pkg install libjpeg-turbo python micro -y
pip install --upgrade pip wheel setuptools
pip install --upgrade tgcf
tgcf --version
tgcf --help
