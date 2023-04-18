import requests
import json

data = requests.get("https://api.hypixel.net/resources/skyblock/items")

with open('items.json', 'w') as outfile:
    json.dump(data.json(), outfile)

with open('items.json') as json_file:
   items = json.load(json_file)

json_object = json.dumps(items, indent=4)
 
# Writing to sample.json
with open("items.json", "w") as outfile:
    outfile.write(json_object)

for i in range(3928, 3999):
    print(items["items"][i]["name"]+", ID: ")
