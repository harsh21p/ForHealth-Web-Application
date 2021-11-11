
import mysql.connector
 
#  function to convert data
def convert_data(data, file_name):
    # Convert binary format to images
    # or files data(with given file_name)
    with open(file_name, 'wb') as file:
        file.write(data)
try:
    # establish connection
    connection = mysql.connector.connect(host='localhost',
                                         database='geeksforgeeks',
                                         user='root',
                                         password='shubhanshu')
    cursor = connection.cursor()
    # getting data by id value 
    query = """ SELECT * from demo where id = %s """
 
    id = 1
    cursor.execute(query, (id,))
    records = cursor.fetchall()
    for row in records:
        print("Person Id = ", row[0])
        print("Person Name = ", row[1])
        image = row[2]
        file = row[3]
        # Pass path with filename where we want to save our file
        convert_data(image, "D:\GFG\images\One.png")
        # Pass path with filename where we want to save our file
        convert_data(file, "D:\GFG\content.txt")
 
    print("Successfully Retrieved Values from database")
 
except mysql.connector.Error as error:
    print(format(error))
 
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")