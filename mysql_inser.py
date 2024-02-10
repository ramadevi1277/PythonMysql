import mysql.connector


mydb = mysql.connector.connect(
    user="root",
    password="Passw0rd",
    database="python_mysql",
    host="localhost",
    port="3306"
)


mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE Laptop(
                    Id int,
                    Name varchar(225),
                    Price int,
                    purchase_date varchar(225)
                    );""")
#mycursor.execute("""INSERT INTO Laptop(Id, Name, Price, Purchase_date)
 #                   VALUES
  #                  (15, "Lenovo", 60000, '2024-01-01')""")


#Adding multiple entries
insert_query = """INSERT INTO Laptop(Id, Name, Price, Purchase_date)
                    VALUES
                    (%s,%s,%s,%s)"""

args = [
    (16, "Dell", 100000, '2012-01-01'),
    (17, "HP", 200000, '2022-02-02'),
    (18, "Dell", 300000, '2023-03-05'),
    (19, "HP", 50000, '')
     ]
mycursor.executemany(insert_query, args)

print(mycursor.rowcount, "Record inserted successfully into Laptop table")

mydb.commit()


mycursor.close()