#Tip Calculator

print("Welcome to the Tip Calculator")

total_bill = float(input("What was the total Bill in Kes\n"))

percentage_tip = int(input("What percantage tip would you like to give\n"))

split_bill = int(input("How Many people to split the bill\n"))

split_bill1 = total_bill/ split_bill

percentage_tip1 = ((percentage_tip / 100) * split_bill1)

final_bill = round(split_bill1 + percentage_tip1, 2)

print(f"Your final bill per person is {final_bill}")