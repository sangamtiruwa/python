'''Write a program that asks the user to enter the area code (for example FI) and
prints out the airports located in that country ordered by airport type. For example, Finland has
65 small airports, 15 helicopter airports and so on.'''

import mysql.connector

connection = mysql.connector.connect(
         host='localhost',
         port=3306,
         database='flight_game',
         user='root',
         password='3790',
         autocommit=True
         )

area_code = input("Enter the are code to search airport: ")
sql = ("select name, type, iso_country from airport order by type asc;")
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
if result:
    for name, type, iso_country in result:
        if area_code == iso_country:
            print(f"The airport {name} is {type}. ")
else:
    print("Invalid!")


cursor.close()
connection.close()