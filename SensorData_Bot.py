from random import random
import sqlite3
import time

db=sqlite3.connect("Database.db",check_same_thread=False)
db.row_factory = sqlite3.Row
cursor=db.cursor()
j=1
while True:
    cursor.execute("INSERT INTO sdata(value1) VALUES((?))",(random(),))
    db.commit()
    print("Done")
    time.sleep(0.1)
    
