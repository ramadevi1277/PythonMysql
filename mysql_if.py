import mysql.connector


mydb = mysql.connector.connect(
    user="root",
    password="Passw0rd",
    database="python_mysql",
    host="localhost",
    port="3306"
)


mycursor = mydb.cursor()

query = """select count(*) from Laptop where Price <= 200000;"""




mycursor.execute(query)

result = mycursor.fetchall()

IF result > 3 TH


