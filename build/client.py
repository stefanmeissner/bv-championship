import json
import requests
from http.client import HTTPSConnection
from config import cfg

GITHUB_API = "api.github.com"
CONTENTS_ENDPOINT = "/repos/RobertPazurek/bv-championship/contents/"

HEADERS = {
    'User-Agent' : 'Python Meisi Build',
    'Authorization' : 'token %s' %  cfg['github']['access_token']
    }

def get(url):
    c = HTTPSConnection(GITHUB_API)
    c.request('GET', url, headers=HEADERS)
    res = c.getresponse()
    data = res.read()
    
    return json.loads(data.decode('utf8'))

def put(url, jsonData):
    requests.put(url, json=jsonData, headers=HEADERS)