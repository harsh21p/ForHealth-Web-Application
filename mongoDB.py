from pymongo import MongoClient
import pymongo
import sqlite3

# Database connection method ... 

def get_database():
    
    CONNECTION_STRING = "mongodb+srv://harshad:harshad@cluster0.9nhrp.mongodb.net/bank?retryWrites=true&w=majority"
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    return client['forhealth']

# main method ...

if __name__ == "__main__":  

    dbname = get_database()

    collection_name = dbname["forhealth"]

    
    # Sql connection ...

    db = sqlite3.connect("Database.db", check_same_thread=False)
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute( "SELECT * FROM info1")
    data = cursor.fetchall()

    for i in data:
        
        item = {
                    "name" : "name_user",
                    "password" : i['password_user'],
                   
                }

        # insert data into database 
     
        collection_name.insert_one(item)

