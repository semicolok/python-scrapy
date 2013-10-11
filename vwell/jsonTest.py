import json

jsonDate = open('../medicalList.json')
data = json.load(jsonDate)
jsonDate.close()

d1 =  data[0]
# print d1

print d1['phone']
print d1['address'].encode('utf-8')
