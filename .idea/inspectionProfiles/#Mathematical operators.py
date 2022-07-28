#Mathematical operators
#BMI Calculator BMI - Body Mass Index
#print BMI as a whole number-  thats why I have used int in the print function
#BMI = weight/height
#data_1 is weight
#data_2 is height

print("Welcome to BMI Calculator")
data_1 = float(input("What is your weight in Kilograms\n"))
data_2 = float(input("Please enter your height in Meters\n"))
BMI = int(data_1 / data_2**2)

print("Your BMI is " + str(BMI))