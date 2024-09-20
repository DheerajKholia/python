import mysql.connector
db = mysql.connector.connect(
    host="localhost", user="root", password="root"
)
print(db)
mycursor = db.cursor()
mycursor.execute("SELECT * FROM pythontestdb.test_table")

for i in mycursor.fetchall():
    print(i)