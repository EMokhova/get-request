import requests
from pprint import pprint

url_hulk = "https://superheroapi.com/api/2619421814940190/search/Hulk"
url_capitan = "https://superheroapi.com/api/2619421814940190/search/Captain America"
url_thanos = "https://superheroapi.com/api/2619421814940190/search/Thanos"

resp1 = requests.get(url_hulk)
resp2 = requests.get(url_capitan)
resp3 = requests.get(url_thanos)
#pprint(resp1.json())
#pprint(resp2.json())
#pprint(resp3.json())

name1 = resp1.json()['results'][0]['name']
name2 = resp2.json()['results'][0]['name']
name3 = resp3.json()['results'][0]['name']
intelligence1 = resp1.json()['results'][0]['powerstats']['intelligence']
intelligence2 = resp2.json()['results'][0]['powerstats']['intelligence']
intelligence3 = resp3.json()['results'][0]['powerstats']['intelligence']

heroes = {name1: intelligence1, name2: intelligence2, name3: intelligence3}
print(heroes)

print(f'Самый умный супергерой - {max(heroes, key=heroes.get)}')



