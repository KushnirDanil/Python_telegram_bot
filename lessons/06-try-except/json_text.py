import json

data = {
    'Name': 'Mir',
    'City': 'K-P',
    'Hobbies': ['reading', 'walking']
}

with open('json.txt','w') as file:
    json.dump(data, file)

with open('json.txt','r') as file:
    data_file = json.load(file)
    print(data_file)

print(data_file['Name'])