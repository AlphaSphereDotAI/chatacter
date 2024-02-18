import matplotlib.pyplot as plt
import os, glob, gradio
from SadTalker.inference import main

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
# os.system("source activate chatacter")
os.system("nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader")
os.system("python --version")
os.chdir("SadTalker")
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

# selected audio from exmaple/driven_audio
img = "examples/source_image/{}.png".format(default_head_name)
print(img)

gradio.inputs.Image(type="pil", label="Source Image")
gradio.outputs.Video(label="Animated Video")
gradio.Interface(
    fn=main(
        img,
        "examples/driven_audio/bus_chinese.wav",
        "examples/source_image/{}.png".format(default_head_name),
    ),
    inputs="image",
    outputs="video",
).launch()
