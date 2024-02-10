import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    password="Passw0rd",
    port="3306",
    database="python_mysql",
    user="root"
)

mycursor = mydb.cursor()

mycursor.callproc('getUserName', [1, ])

results = mycursor.stored_results()

print(results)
for each in results:
    print(each.fetchone())



mycursor.close()
mydb.close()