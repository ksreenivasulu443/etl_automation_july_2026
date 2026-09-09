d = {}

d1 =dict()

print("d details", d, id(d), type(d), dir(d), d.__sizeof__())

print("d1 details", d1, id(d1), type(d1), dir(d1), d1.__sizeof__())

# d2 = {key:value, ke2:value, ......}

d2 = {'1':'sreeni', '2':'Rahul', 3:'Ramya', 4:'Nandini'}

print("d2 details", d2, id(d2), type(d2), dir(d2), d2.__sizeof__())

d2[5] = 'Hari' # adding new key value pair

d2.update({6:'Janav', 2:'Wahal', 5:'Hari'})

print("d2 details after adding new pair", d2, id(d2))

print("key 1 value", d2.get(1), d2[1]) # 1 is key not index

print("key 6 value", d2.get(6), d2[6])

print("key 7 value", d2.get(7) )

print("key 7 value", d2[1])

print("keys in d2", d2.keys(), type(d2.keys()))
print("values in d2", d2.values(), type(d2.values()))
print("values in d2", d2.items(), type(d2.items()))

d2.pop(6)

print("d2 details after pop", d2, id(d2))

d2.popitem()

print("d2 details after popitem", d2, id(d2))



d3 = {
   1: "Joe",
   "lastName": "Jackson",
   "gender": "male",
   "age": 28,
   "address": {
       "streetAddress": "101",
       "city": "San Diego",
       "state": "CA"
   },
   "phoneNumbers": [
       	{"type": "home", "number": "7349282382" },
	    {"type": "office", "number": "7123456" },
        {"type": "office2", "number": "71234565555" },
       {"type": "home2", "number": "534534534" }

   ]
}

print(d3['phoneNumbers'][0]['number'])

x = ('key1', 'key2', 'key3')
y = (1,2,3)

thisdict = dict.fromkeys(x, y)

print(thisdict)



car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

