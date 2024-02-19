import os

'''
apt-get update
apt install software-properties-common -y
dpkg --remove --force-remove-reinstreq python3-pip python3-setuptools python3-wheel
apt-get install python3-pip -y
apt autoremove -y
git clone https://github.com/Winfredy/SadTalker
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 \
--extra-index-url https://download.pytorch.org/whl/cu113
apt update
apt install ffmpeg -y
'''

# Now, the virtual environment is created and you can install packages using pip.
# os.system("source activate chatacter")
os.system("nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader")
os.system("python --version")
os.chdir("sadtalker")
# os.system("pip install -r requirements.txt")

print("Download pre-trained models...")
if not os.path.exists("checkpoints"):
    print("Download pre-trained models...")
    os.system("rm -rf checkpoints")
    os.system("bash scripts/download_models.sh")
else:
    print("Pre-trained models already exist.")

image = "examples/source_image/art_0.png"
audio = "examples/driven_audio/bus_chinese.wav"
results = "results"
os.system(f"python inference.py \
            --source_image {image} \
            --driven_audio {audio} \
            --checkpoint_dir checkpoints \
            --result_dir {results}")

# gradio.Interface(
#     fn=,
#     inputs='textbox',
#     outputs='video',
# ).launch()
