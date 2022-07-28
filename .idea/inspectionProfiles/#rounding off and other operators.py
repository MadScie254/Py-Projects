#rounding off and other operators
print(round(9/2)) #here we have rounded off to the nearest integer

print(round(10/3, 2)) #the ans is rounded off to 2 decimal places. Comma is used to specify the number of decimal spaces
print(round(2.66666666, 2))

print(9//2) #here the // sign is used to eliminate any floats or decimals from the answer


marks = 2
marks /= 2 #/= means divide marks by 2
print(marks)

#Use of an f-String string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values
score = 80
height = 1.8
isWinning = True
#lets use the fstring to combine rather than the plus sign

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")




