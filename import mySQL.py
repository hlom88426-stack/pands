import mySQL.connector
mydb=mySQL.connector.connect (
host="Localhost",
user="root",
password="123"
)
mycursor =mydb. cursor()
mycursor.execute("CREATE DATABASE COLLEGE")