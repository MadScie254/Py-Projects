#Program that can tell us how many days weeks and months we have left if we were lucky to live till 90yrs
#current age
#1 year = 365 days
# #weeks = 52
#months = 12

print("Welcome to time remaining calculator")
current_age = int(input("What is current age\n"))
age_expected = int(input("Enter age expected to live\n"))

no_of_months_in_age_expected = age_expected * 12

no_of_weeks_in_age_expected = age_expected * 52

no_of_days_in_age_expected = age_expected * 365


months_remaining = no_of_months_in_age_expected - (current_age * 12)

weeks_remaining = no_of_weeks_in_age_expected - (current_age * 52)

days_remaining = no_of_days_in_age_expected - (current_age * 365)

message = f"You have {months_remaining} months, {weeks_remaining} weeks, {days_remaining} days remaining"

print(message)


  