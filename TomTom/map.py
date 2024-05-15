import sys
import urllib.request
import json

apiKey = "DfnN8Blh43zXpIAOYanoTd7Yy8n2pKU7"
zoom = "100"
city = "manila"
size = "large"

url = f'https://api.tomtom.com/search/2/search/{city}.json?idxSet=Geo&key={apiKey}'

req = urllib.request.urlopen(url)
data = req.read().decode('utf-8')

obj = json.loads(data)

if (len(obj['results']) == 0):
  print("City Not Found!")
  quit()

print(f"Found City Center Of {city} at {str(obj['results'][0]['position'])}")

lat = obj['results'][0]['position']['lat']
lon = obj['results'][0]['position']['lon']

switcher = {
  'small': '&width=256&height=256',
  'medium': '&width=512&height=512',
  'large' :'&width=1024&height=1024',
}

urlStaticImage = f"https://api.tomtom.com/map/1/staticimage?layer=basic&style=main&format=png&zoom={zoom}&center={str(lon)},{str(lat)}{switcher.get(size)}&key={apiKey}"

print(urlStaticImage)