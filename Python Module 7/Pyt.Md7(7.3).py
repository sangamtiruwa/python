'''3.Write a program for fetching and storing airport data. The program asks the user if they want
to enter a new airport, fetch the information of an existing airport or quit. If the user chooses to enter a
new airport, the program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch
airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name. If the
user chooses to quit, the program execution ends. The user can choose a new option as many times they want until they choose to quit.
(The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
You can easily find the ICAO codes of different airports online.)'''


airport_data = {}

while True:
    print("\nAirport Data Program")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        icao_code = input("Enter the ICAO code of the airport: ")
        airport_name = input("Enter the name of the airport: ")
        airport_data[icao_code] = airport_name
        print("Airport information saved.")

    elif choice == "2":
        icao_code = input("Enter the ICAO code to fetch airport information: ")
        if icao_code in airport_data:
            print(f"The name of the airport with ICAO code {icao_code} is {airport_data[icao_code]}.")
        else:
            print(f"Airport with ICAO code {icao_code} not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
