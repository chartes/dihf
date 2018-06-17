# -*- coding: utf-8 -*-
import sys, requests, json

# utilitaire quick-and-dirty pour les API Gallica/BnF

def ark2manifest(ark):
	manifest = ark[:ark.index("ark")] + "iiif/" + ark[ark.index("ark"):] + "/manifest.json"
	return manifest

# pour chaque arK Gallica de la liste, infère du manifeste IIIF le nombre d’images
if sys.argv[1] == "imgCount":
	with open('arkList.txt') as f:
		for line in f:
			ark = line.strip()
			manifestURL = ark2manifest(ark)
			manifest = requests.get(manifestURL)
			j = json.loads(manifest.text)
			print ark + "	" + str(len(j['sequences'][0]["canvases"]))

# pour chaque arK Gallica de la liste, enregistre le PDF correspondant
elif sys.argv[1] == "getPDF":
	with open('arkList.txt') as f:
		for line in f:
			ark = line.strip()
			pdfURL = ark+".pdf"
			pdfName = ark.rsplit('/', 1)[-1]+".pdf"
			r = requests.get(pdfURL)
			with open(pdfName, 'wb') as pdf:
				pdf.write(r.content)
			print pdfName+" OK"

else:
	print "arg: imgCount|getPDF"
