import mysql.connector
db = mysql.connector.connect(
    host="localhost", user="root", password="root"
)
print(db)
mycursor = db.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
mycursor.execute("CREATE DATABASE IF NOT EXISTS test2")
mycursor.execute("create table test2.test_table (c1 INT, c2 VARCHAR(50), c3 INT, c4 FLOAT, c5 VARCHAR(40))")
db.close()