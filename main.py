from base64 import b64encode
from sys import argv
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'

img_requests = [] #送信するファイル

with open("receipt1.jpg", 'rb') as f:
    # ctxt = b64encode(f.read()) ＃デコードするとprintで表示された　要仕様確認
    ctxt = b64encode(f.read()).decode() #base64エンコード
    img_requests.append({
        'image': {'content': ctxt},
        'features': [{
            'type': 'TEXT_DETECTION	',
            'maxResults': 10
        }]
    })
    # print(img_requests)
    # print(ctxt)
    
f.close()
print("finish")