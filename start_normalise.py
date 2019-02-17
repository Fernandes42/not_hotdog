# Removing all files that aren't .jgp, thid was meant to make translation to numpy array easiers. Very bad code on my part though. Will fix later

from PIL import Image
import os

url_path = "/Users/josh/Hackathons/ru_hacking/downloads/Not hotdog/"
for filename in os.listdir(url_path):
    if filename.endswith(".png") or filename.endswith(".ash") or filename.endswith(".webp") or filename.endswith(".web") or filename.endswith(".tif") or filename.endswith(".gif"):
        continue
    else:
        try:
            Image.open(url_path+filename).convert('RGB').save(url_path+'RGB'+filename)
        except:
            continue
        os.remove(url_path+filename)
    continue
