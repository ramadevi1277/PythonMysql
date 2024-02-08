import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    password="Passw0rd",
    user="root",
    port="3306",
    database="python_mysql"
)

my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM USERS;")

result = my_cursor.fetchall()

print(result)


my_cursor.close()
mydb.close()