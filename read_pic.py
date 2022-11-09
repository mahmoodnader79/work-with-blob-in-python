
from asyncio.windows_events import NULL
import mysql.connector
import io
from PIL import Image
import sqlite3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(empId, name, photo, resumeFile):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        try:
            cursor.execute("CREATE TABLE new_employee ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL, resume BLOB NOT NULL);")
            print ("Table created successfully")
        except:
            pass
        sqlite_insert_blob_query = """ INSERT INTO new_employee
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(photo)
        resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        print("empPhoto",empPhoto)
        print("resume",resume)
        
        data_tuple = (empId, name, empPhoto, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")


insertBLOB(7, "api-security", "api-security.png", "api-security_resume.txt")

# conn.execute("CREATE TABLE new_employee ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL, resume BLOB NOT NULL);")
# print ("Table created successfully")
# Function for Convert Binary
# Data to Human Readable Format


# #insert to mysql files
# def convertToBinaryData(filename):
#     # Convert digital data to binary format
#     with open(filename, 'rb') as file:
#         binaryData = file.read()
#     return binaryData
# def convertToBinaryData(filename):
#     # Convert digital data to binary format
#     with open(filename, 'rb') as file:
#         binaryData = file.read()
#     return binaryData



def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def readBlobData(empId):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
        cursor.execute(sql_fetch_blob_query, (empId,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name = row[1]
            photo = row[2]
            resumeFile = row[3]

            print("Storing employee image and resume on disk \n")
            photoPath = "C:\\Users\\asus\\Desktop\\file_project\\new\\" + name + ".jpg"
            resumePath = "C:\\Users\\asus\\Desktop\\file_project\\new\\" + name + "_resume.txt"
            writeTofile(photo, photoPath)
            writeTofile(resumeFile, resumePath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
readBlobData(7)





# def insertBLOB(emp_id, name, photo, biodataFile):
#     print("Inserting BLOB into python_employee table")
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                                              database='pic',
#                                              user='root',
#                                              password='')

#         cursor = connection.cursor()
#         sql_insert_blob_query = """ INSERT INTO python_employee
#                           (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""

#         empPicture = convertToBinaryData(photo)
#         file = convertToBinaryData(biodataFile)

#         # Convert data into tuple format
#         insert_blob_tuple = (emp_id, name, empPicture, file)
#         result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
#         connection.commit()
#         print("Image and file inserted successfully as a BLOB into python_employee table", result)

#     except mysql.connector.Error as error:
#         print("Failed inserting BLOB data into MySQL table {}".format(error))

#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")

# insertBLOB(1, "Eric", "C:\\Users\\asus\Desktop\\types-of-api.png",
#            "C:\\Users\\asus\\Desktop\\types-of-api.txt")


# connection=mysql.connector.connect(host="localhost",
#                  user="root",
#                  passwd="",
#                  db="pic")
# cursor=connection.cursor()
# sql1 = 'select * from python_employee'
# cursor.execute(sql1)
# data2 = cursor.fetchall()

# file_like2 = io.BytesIO(data2[0][0])

# img1=Image.open(file_like2)
# img1.show()
# cursor.close()
# connection.close()

