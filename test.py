import json

conf = open('config.json', "r")
confs = json.load(conf)
print(confs['token'])
