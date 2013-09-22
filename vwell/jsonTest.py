import json

jsonDate = open('../medicals.json')
data = json.load(jsonDate)
jsonDate.close()
d1 =  data[0]
print d1.keys()

for key in d1.keys():
	print key
print d1['phone'].encode('utf-8')
print d1['address'].encode('utf-8')
