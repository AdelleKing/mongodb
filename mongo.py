import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "MyFrstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s")% e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

print(coll)

documents = coll.find()

new_doc = {
    "first": "douglas",
    "last": "adams",
    "dob": "11/03/1952",
    "gender": "m",
    "hair_color": "grey",
    "occupation": "writer",
    "nationality": "british"
}
coll.insert_one(new_doc)



print(documents)
