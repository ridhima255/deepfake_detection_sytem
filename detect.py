import cv2
import numpy as np
from tensorflow.keras.models import load_model

# load trained model
model = load_model("model/deepfake_model.h5")

def predict_image(img_path):

    img = cv2.imread(img_path)
    img = cv2.resize(img,(128,128))
    img = img/255.0
    img = np.reshape(img,(1,128,128,3))

    prediction = model.predict(img)

    if prediction[0][0] > 0.5:
        return "Fake"
    else:
        return "Real"