#Data Types

#Strings

print("Hello"[0])

print("Hello"[4])

#Integer
print(123+345)

#In oythin commas arent used to split huge numbers while under score are used
r = 123_435_567

#float
example = 3.142

#changing variable type
#Creating a character number counter
num_char = len(input("What is your name?\n"))
new_num_char = str(num_char)

print("Your name has " + new_num_char + " Characters")

#proram that adds two digit number
number  = input("Type a seven digit random number\n")
first_digit = number[0]
second_digit = number[1]
third_digit = number[2]
fourth_digit = number[3]
five_digit = number[4]
six_digit = number[5]
seven_digit = number[6]
output_ans = int(first_digit) + int(second_digit) +int(third_digit) + int(fourth_digit) + int(five_digit) + int(six_digit) + int(seven_digit)
print(output_ans)

