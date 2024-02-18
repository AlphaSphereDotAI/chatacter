import ipywidgets as widgets
import matplotlib.pyplot as plt
from IPython.display import HTML
from IPython.display import display
from base64 import b64encode
import os, sys, glob
import gradio

# apt-get update
# apt install software-properties-common -y
# dpkg --remove --force-remove-reinstreq python3-pip python3-setuptools python3-wheel
# apt-get install python3-pip -y
# apt autoremove -y
# git clone https://github.com/Winfredy/SadTalker
# pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
# apt update
# apt install ffmpeg -y

# Now, the virtual environment is created and you can install packages using pip.
os.system("source activate chatacter")
os.system("nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader")
os.system("python --version")
os.system("cd SadTalker")
os.system("pip install -r requirements.txt")

print("Download pre-trained models...")
if not os.path.exists("checkpoints"):
    print("Download pre-trained models...")
    os.system("rm -rf checkpoints")
    os.system("bash scripts/download_models.sh")
else:
    print("Pre-trained models already exist.")


print("Choose the image name to animate: (saved in folder 'examples/')")
img_list = glob.glob1("examples/source_image", "*.png")
img_list.sort()
img_list = [item.split(".")[0] for item in img_list]
default_head_name = "art_0"


def on_change(change):
    if change["type"] == "change" and change["name"] == "value":
        plt.imshow(plt.imread("examples/source_image/{}.png".format(default_head_name)))
        plt.axis("off")
        plt.show()


# selected audio from exmaple/driven_audio
img = "examples/source_image/{}.png".format(default_head_name)
print(img)
os.system(
    "python inference.py --driven_audio ./examples/driven_audio/RD_Radio31_000.wav \
           --source_image {img} \
           --result_dir ./results --still --preprocess full --enhancer gfpgan"
)
