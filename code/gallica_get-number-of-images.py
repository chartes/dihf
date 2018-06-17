import requests
import json


def ark2manifest(ark):
	manifest = ark[:ark.index("ark")] + "iiif/" + ark[ark.index("ark"):] + "/manifest.json"
	return manifest

with open('arkList.txt') as f:
	for line in f:
		ark = line.strip()
		manifestURL = ark2manifest(ark)
		manifest = requests.get(manifestURL)
		j = json.loads(manifest.text)
		print ark + "	" + str(len(j['sequences'][0]["canvases"]))
