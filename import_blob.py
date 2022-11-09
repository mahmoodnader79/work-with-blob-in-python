import mysql.connector
import sqlite3
connection = mysql.connector.connect(host='localhost',
                                             database='pic',
                                             user='root',
                                             password='')

cursor = connection.cursor()
cursor.execute("SELECT `name`, `photo`, `biodata` FROM `python_employee`")
x = cursor.fetchall()
sqliteConnection = sqlite3.connect('SQLite_Python.db')
cursor = sqliteConnection.cursor()
sqlite_insert_blob_query = """ INSERT INTO new_employee
                                  (name, photo, resume) VALUES (?, ?, ?)"""
cursor.execute(sqlite_insert_blob_query, x)
sqliteConnection.commit()
print("Image and file inserted successfully as a BLOB into a table")
cursor.close()