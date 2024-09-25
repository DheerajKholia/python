from pymongo import MongoClient
client = MongoClient('mongodb://mongoadmin:mongopasswd@localhost:27017')
print(client)

#create DB
db = client["mongotestDB"]
data = {
    "name": "John",
    "department" : "Accounts",
    "status" : "Active"
}

data2 = {
    "name": "Ron",
    "department" : "HR",
    "status" : "Active"
}
data3 = {
    "name": "Steeve",
    "department" : "Accounts",
    "status" : "Active"
}
collection = db["my_test_record"]
collection.insert_one(data)
collection.insert_one(data2)

#Find collections
for d in collection.find():
    print(d)

#Filtered data
for i in collection.find({'department': 'Accounts'}):
    print(i)

for i in collection.find({'_id': {'$gte' : '4'}}):
    print(i)

#Update a record
collection.update_many({'department':'Accounts'}, {'$set':{'department':'Finance'}})
#Delete collection
# collection.drop()