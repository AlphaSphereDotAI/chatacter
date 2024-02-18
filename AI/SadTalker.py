import ipywidgets as widgets
import matplotlib.pyplot as plt
from IPython.display import HTML
from IPython.display import display
from base64 import b64encode
import os, sys, glob
import venv
import getpass
import subprocess

password = getpass.getpass()
venv_dir = "../.virtualenv"
builder = venv.EnvBuilder(with_pip=True)
builder.create(venv_dir)

# Now, the virtual environment is created and you can install packages using pip.
# os.system('echo %s|sudo -S %s' % (password, 'source .virtualenv/bin/activate'))
os.system('nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader')

# Commented out IPython magic to ensure Python compatibility.
# os.system('update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.8 2')
# os.system('update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.9 1')
# os.system('sudo apt install python3.8')
# os.system('sudo apt-get install python3.8-distutils')

subprocess.run(['sudo', '-S', 'python', '--version'], input=password, text=True)
os.system('python --version')
# os.system('echo %s|sudo -S %s' % (password, 'apt-get update'))
# os.system('echo %s|sudo -S %s' % (password, 'apt install software-properties-common -y'))
#
# os.system('echo %s|sudo -S %s' % (password, 'dpkg --remove \
# --force-remove-reinstreq python3-pip python3-setuptools python3-wheel'))
# os.system('echo %s|sudo -S %s' % (password, 'apt-get install python3-pip -y'))
# os.system('echo %s|sudo -S %s' % (password, 'apt autoremove -y'))
#
# print('Git clone project and install requirements...')
# os.system('echo %s|sudo -S %s' % (password, 'git clone https://github.com/Winfredy/SadTalker &> /dev/null'))
# os.system('cd SadTalker')
# # os.system('echo %s|sudo -S %s' % (password, 'export PYTHONPATH=/content/SadTalker:$PYTHONPATH'))
# os.system('echo %s|sudo -S %s' % (password, 'pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 \
#     --extra-index-url https://download.pytorch.org/whl/cu113'))
# os.system('echo %s|sudo -S %s' % (password, 'apt update'))
# os.system('echo %s|sudo -S %s' % (password, 'apt install ffmpeg -y &> /dev/null'))
# os.system('pip install -r requirements.txt')
#
# print('Download pre-trained models...')
#
# if not os.path.exists('checkpoints'):
#     print('Download pre-trained models...')
#     os.system('rm -rf checkpoints')
#     os.system('bash scripts/download_models.sh')
# else:
#     print('Pre-trained models already exist.')
#
# # borrow from makeittalk
#
# print("Choose the image name to animate: (saved in folder 'examples/')")
# img_list = glob.glob1('examples/source_image', '*.png')
# img_list.sort()
# img_list = [item.split('.')[0] for item in img_list]
# default_head_name = 'art_0'
#
#
# def on_change(change):
#     if change['type'] == 'change' and change['name'] == 'value':
#         plt.imshow(plt.imread('examples/source_image/{}.png'.format(default_head_name.value)))
#         plt.axis('off')
#         plt.show()
#
#
# default_head_name.observe(on_change)
# display(default_head_name)
# plt.imshow(plt.imread('examples/source_image/{}.png'.format(default_head_name.value)))
# plt.axis('off')
# plt.show()
#
# """Animation"""
#
# # selected audio from exmaple/driven_audio
# img = 'examples/source_image/{}.png'.format(default_head_name.value)
# print(img)
# os.system('python inference.py --driven_audio ./examples/driven_audio/RD_Radio31_000.wav \
#            --source_image {img} \
#            --result_dir ./results --still --preprocess full --enhancer gfpgan')
#
# # get the last from results
# results = sorted(os.listdir('./results/'))
#
# mp4_name = glob.glob('./results/*.mp4')[0]
#
# mp4 = open('{}'.format(mp4_name), 'rb').read()
# data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
#
# print('Display animation: {}'.format(mp4_name), file=sys.stderr)
# display(HTML("""
#   <video width=256 controls>
#         <source src="%s" type="video/mp4">
#   </video>
#   """ % data_url))
