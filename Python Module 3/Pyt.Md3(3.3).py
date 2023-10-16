'''3. Write a program that asks for the biological gender and hemoglobin value (g/l). The program
notifies the user if the hemoglobin value is low, normal or high.
A normal hemoglobin value for adult females is between 117-155 g/l.
A normal hemoglobin value for adult males is between 134-167 g/l.'''

user = input("Enter the biological gender(female/male) : ")
Hemoglobin = float(input("What is the hemoglobin value (g/l)?: "))
if (user == 'female'):
    if (Hemoglobin < 117):
        print("Hemoglobin value is low.")
    elif (Hemoglobin >= 117 and Hemoglobin <= 155):
        print("Its normal for adult female.")
    elif (Hemoglobin > 155):
         print("Hemoglobin value is high.")


if (user == 'male'):
    if (Hemoglobin < 134):
        print("Hemoglobin value is low.")
    elif (Hemoglobin >= 134 and Hemoglobin <= 167):
           print("Its normal for adult male.")
    elif (Hemoglobin > 167):
          print("Hemoglobin value is high.")

else:
     print("Invalid Input.")
