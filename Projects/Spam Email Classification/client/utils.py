import requests
import json

url = "http://127.0.0.1:8080"

def predict(email):
    data = {
        'email': email
    }
    response = requests.post(f'{url}/get_prediction',data=json.dumps(data))
    pred = response.json()['data']
    color = None
    if pred == "spam":
        color = "red"
    elif pred == "ham":
        color = "green"
    return pred, color