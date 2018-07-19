import config

CONFIG_PATH = "config_sme.yml"
config.load(CONFIG_PATH)

import client
import updateContent
import base64

PATH = "points_meisi.txt"

URL = "https://"+config.cfg['github']['api']+config.cfg['github']['contents_endpoint']+PATH

oldFile = client.get(URL)
sha = oldFile['sha']
print(sha)

#jsonData = updateContent.updatePath(URL, "new Champion Points for Meisi", "4", sha)
#client.put(URL, jsonData)