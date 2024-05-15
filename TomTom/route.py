import urllib.request
import json

apiKey = "DfnN8Blh43zXpIAOYanoTd7Yy8n2pKU7"
versionNumber = "1"

url = f"https://api.tomtom.com/traffic/trafficstats/routeanalysis/{versionNumber}?key={apiKey}"

req = urllib.request.urlopen(url)
data = req.read().decode("utf-8")

obj = json.loads(data)



print(obj)