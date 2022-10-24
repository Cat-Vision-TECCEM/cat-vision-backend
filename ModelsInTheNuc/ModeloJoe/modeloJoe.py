import json
import tensorflow as tf
import numpy as np
from tensorflow import keras
import os


model_path = "saved_model.pb"
model = tf.keras.models.load_model("Modelojoe/savemodels")

classes = ['fanta', 'leche']
skus = os.listdir("./skusForProcess")
def prediction():
    jsonSku = {}
    for sku in skus:    
        image = keras.utils.load_img("./skusForProcess/"+sku, target_size=(224,224,3))
        image_array = tf.expand_dims(keras.utils.img_to_array(image), 0)
        predictions = model.predict(image_array)
        score = tf.nn.softmax(predictions[0])
        #print(classes[np.argmax(score)], 100 * np.max(score))
        if classes[np.argmax(score)] not in jsonSku:
            jsonSku[classes[np.argmax(score)]] = 1
        else:
            jsonSku[classes[np.argmax(score)]] += 1
    return jsonSku

