import mysql.connector
db = mysql.connector.connect(
    host="localhost", user="root", password="root"
)
print(db)
mycursor = db.cursor()
mycursor.execute("INSERT INTO pythontestdb.test_table values(3214, 'John', 23455, 244.24, 'Doe')")
mycursor.execute("INSERT INTO pythontestdb.test_table values(2214, 'Ron', 255, 244.24, 'Doe')")
mycursor.execute("INSERT INTO pythontestdb.test_table values(1214, 'Jenny', 1455, 244.24, 'Doe')")
mycursor.execute("INSERT INTO pythontestdb.test_table values(0214, 'Johnson', 455, 244.24, 'Doe')")
db.commit()
db.close()