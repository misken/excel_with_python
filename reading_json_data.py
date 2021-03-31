import json

json_data = open('data/data-text.json').read()

data = json.loads(json_data)
print(type(data))

for item in data:
    print(item)