'''Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the database. Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.

'''
from geopy.distance import geodesic
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Seagates',
         autocommit=True
         )

cursor = connection.cursor()
Icao_code1 = input("Enter First ICAO code of an airport : ")
Icao_code2 = input("Enter Second ICAO code of an airport : ")

cursor.execute("select latitude_deg, longitude_deg from ariport where ident = {icao_code1}"
airport1_cords = cursor.fetchone()
cursor.execute("select latitude_deg, longitude_deg from ariport where ident = {icao_code2}")
airport2_cords = cursor.fetchone()

cursor.close()
connection.close()