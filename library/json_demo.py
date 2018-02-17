import json

# sample string of JSON
person = '{"name":"Madan", "mobile":"7893559018"}'

# 'loads' method takes string of JSON and converts to python 'dictionary' or 'list'
s = json.loads(person)
print(type(s))
print(s["mobile"])

print()

contact = '{"name":"Srikanth", "mobile":["9059057000","9849125256"]}'

f = open("contact.txt", "w")
json.dump(contact, f)  # 'dump' method writes to file

f = open("contact.txt", "r")
contact2 = json.load(f)  # 'load' method reads from file. this is different form 'loads' method
print(contact2)
