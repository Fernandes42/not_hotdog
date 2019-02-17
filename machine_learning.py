# This did not end up working, kept crashing after using too much memory. Dataset was probably too large (14000 images)
# As time was issue(Hackathon) used GCP AutoML Vision Instead

import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import sklearn.model_selection as model_selection
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import PIL
from PIL import Image
import numpy as np
print(1)
np_array = []
url_path=["/Users/josh/Hackathons/ru_hacking/downloads/Not hotdog/", "/Users/josh/Hackathons/ru_hacking/downloads/Hotdog/"]
for x in url_path:
    for filename in os.listdir(x):
        try:
            route=(x+filename)
            img = PIL.Image.open(route)
            arr = np.array(img)
            np_array.append(arr)
        except:
            continue

numpy_array = np.asarray(np_array)
print(2)
print(numpy_array.shape)
X = numpy_array

y = []
for x in range(8514):
    y.append(0)
for z in range(3383):
    y.append(1)
print(len(y))
# X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y,train_size=0.75,test_size=0.25, random_state=101)
print(4)
clf = RandomForestClassifier(n_estimators=3, max_depth=5, n_jobs=-1)
clf.fit(X,y)
print(5)
