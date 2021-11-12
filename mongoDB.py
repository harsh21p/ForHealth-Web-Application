import pymongo
from pymongo import MongoClient
import sqlite3

# Database connection method ...

db = sqlite3.connect("Database.db", check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()

CONNECTION_STRING = "mongodb+srv://harshad:harshad@cluster0.9nhrp.mongodb.net/bank?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)

def get_database():
    return client['forhealth']

dbname = get_database()
collection_name = dbname["forhealth"]


def upload_to_database():
   
    # Sql connection ...

    cursor.execute("SELECT * FROM info1")
    data = cursor.fetchall()

    for i in data:

        item = {
            "name": i["name_user"],
            "password": i['password_user'],

        }

        # insert data into database

        collection_name.insert_one(item)
    


def download_from_database():
    for record in collection_name.find().limit(10):
        print(record)
        cursor.execute("UPDATE info1 SET uname=(?),uage=(?),uweight=(?),uheight=(?),selectbtn=(?) WHERE name_user=(?)", (record['name_user'], record['uage'], record['uweight'], record['uheight'], record['selectbtn'], record['name_user']))
    


# main method ...

if __name__ == "__main__":
    upload_to_database()
    download_from_database()
