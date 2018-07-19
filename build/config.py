import yaml

cfg = {}

def load(path):
    global cfg
    with open(path, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
