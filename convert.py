# Normalising data to same size to improve accuracy of machine learning model

from PIL import Image
import os

url_path = "/Users/josh/Hackathons/ru_hacking/downloads/Not hotdog/"
for filename in os.listdir(url_path):
    route = url_path+filename
    if os.path.isfile(route):
        try:
            im = Image.open(route)
            f, e = os.path.splitext(route)
            imResize = im.resize((1000,800), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
            os.remove(route)
        except:
            os.remove(route)

    else:
        continue
