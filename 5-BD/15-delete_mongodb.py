from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

myquery = {"category": "Automação"}
x = mycol.delete_one(myquery)

print(f"{x.deleted_count} documento excluído!")