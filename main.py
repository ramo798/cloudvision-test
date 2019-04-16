from base64 import b64encode
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
api_key = "AIzaSyDvEANhFo30rDRAXcZ88QJmQmqtbbw5Jhc"

img_requests = [] #送信するファイル

with open("./receipt1.jpg", 'rb') as f:
    # ctxt = b64encode(f.read()) ＃デコードするとprintで表示された　要仕様確認
    ctxt = b64encode(f.read()).decode() #base64エンコード
    img_requests.append({
        'image': {'content': ctxt},
        'features': [{
            'type': 'TEXT_DETECTION',
            'maxResults': 10
        }]
    })
    

response = requests.post(
    ENDPOINT_URL,
    data=json.dumps({"requests": img_requests}).encode(),
    params={'key': api_key},
    headers={'Content-Type': 'application/json'}
)
for idx, resp in enumerate(response.json()['responses']):
    print(json.dumps(resp, indent=2))

f.close()