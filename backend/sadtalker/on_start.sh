apt update
apt full-upgrade -y
apt install software-properties-common -y
apt install ffmpeg -y
apt autoremove -y

pip install -U pip
pip install setuptools==59.8.0
pip install torch==2.1.0+cu121 torchvision==0.16.0+cu121 torchaudio basicsr==1.4.2 --use-pep517 --extra-index-url https://download.pytorch.org/whl/cu121
pip install -v -r requirements.txt

sh ./scripts/download_models.sh