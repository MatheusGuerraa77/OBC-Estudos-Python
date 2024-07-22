from pymongo import MongoClient

client = MongoClient()

print(client)
mydb = client.obcblog
mycol = mydb.posts

post1 = {
    "title": "Web Scraping",
    "category": "Automação",
    "author": {
        "name": "Fulano",
        "email": "fulano@email.com"
    }
}

result = mycol.insert_one(post1)
print("Documento incluído com sucesso !")