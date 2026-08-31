import numpy as np
from tensorflow.keras.preprocessing import image
import os

def predict_image(model, img_path, classes, target_size=(150,150)):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"File tida ditemukan:{img_path}")
    
    img=image.load_img(img_path, target_size=target_size)
    img_array=image.img_to_array(img)
    img_array=np.expand_dims(img_array,axis=0)
    img_array=img_array/255.0

    prob=model.predict(img_array, verbose=0)[0][0]

    probabilities={
        classes[0]:float(1-prob),
        classes[1]:float(prob)
    }

    predicted_class=classes[int(prob >0.5)]
    confidence=max(probabilities.values())
    
    return confidence, predicted_class
