apt update
apt install software-properties-common -y
add-apt-repository ppa:jonathonf/ffmpeg-4 -y
apt update
apt install ffmpeg -y
pip install -U pip
pip install torch==1.12.1+cu121 torchvision==0.13.1+cu121 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt --use-pep517 -v