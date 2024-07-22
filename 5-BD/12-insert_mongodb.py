from pymongo import MongoClient

client = MongoClient()

print(client)
mydb = client.obcblog
mycol = mydb.posts

post1 = {
    "title": "FastApi",
    "category": "Backend",
    "author": {
        "name": "Rodrigo",
        "email": "rodrigo@email.com"
    }
}

result = mycol.insert_one(post1)
print("Documento incluído com sucesso !")