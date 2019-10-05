import mysql.connector

db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'root',
	database='new')

if db.is_connected():
	print("hello")
else:
	print("no hello")

# mycursor = db.cursor()