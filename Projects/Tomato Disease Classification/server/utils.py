import json
import base64
import tensorflow as tf
from pydantic import BaseModel


__model = None
__labels = None


class InputSchema(BaseModel):
    image_b64: str


def load_artifacts():
    global __model
    global __labels
    
    model_layer = tf.keras.layers.TFSMLayer("./artifacts/model/", call_endpoint="serving_default")

    __model = tf.keras.Sequential([
        model_layer
                        ])
    with open('./artifacts/labels.json') as f:
        __labels = json.load(f)


def classify(request):
    image_bytes = base64.b64decode(request.image_b64)
    image = tf.io.decode_image(image_bytes,channels=3)
    image = tf.expand_dims(image,0)
    probs = __model.predict(image,verbose=False)
    probs = probs['dense_2']
    probs = tf.squeeze(probs)
    index = tf.argmax(probs,axis=-1).numpy()
    pred_class = __labels['class_names'][index]
    pred_confidence = probs[index]
    pred_confidence = round(pred_confidence.numpy()*100,2)
    return {
        'data': {
            'class': pred_class,
            'confidence': pred_confidence
        }
    }