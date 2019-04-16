from base64 import b64encode
from sys import argv
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'

with open("receipt1.jpg", 'rb') as f:
    ctxt = b64encode(f.read()).decode()
    print(ctxt)
    
f.close()
print("finish")