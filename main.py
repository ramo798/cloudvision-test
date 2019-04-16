from base64 import b64encode
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
api_key = "key.json"

img_requests = [] #送信するファイル

with open("./receipt1.jpg", 'rb') as f:
    # ctxt = b64encode(f.read()) ＃デコードするとprintで表示された　要仕様確認
    ctxt = b64encode(f.read()).decode() #base64エンコード
    img_requests.append({
        'image': {'content': ctxt},
        'features': [{
            'type': 'TEXT_DETECTION	',
            'maxResults': 10
        }]
    })
    
data = json.dumps({"requests": img_requests }).encode()

response = requests.post(
    ENDPOINT_URL,
    data,
    params={'key': api_key},
    headers={'Content-Type': 'application/json'}
)

print(response)

f.close()