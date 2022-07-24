import pymongo
client = pymongo.MongoClient("mongodb+srv://rajput:Anil123@myfirstcluster.iqi1a.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Anil",
    "sname": "Rajput",
    "gmail": "singalanil1995@gmail.com"
}
d = {
    "name": "Anil",
    "sname": "Rajput",
    "gmail": "singalanil1995@gmail.com"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

