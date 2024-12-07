import requests
import base64
import json


url = "http://fastapi:8080"


def classify(file_uploader):
    image_bytes = file_uploader.read()
    image_b64 = base64.b64encode(image_bytes).decode()
    data = {
        'image_b64': image_b64
    }
    json_data = json.dumps(data)
    response = requests.post(url=f'{url}/classify_image', data=json_data)
    content = response.json()['data']
    cls = content['class']
    confidence = content['confidence']

    return cls, confidence
    