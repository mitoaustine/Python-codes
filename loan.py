# Prompt the user for their age and annual income
age = int(input("Enter your age: "))
income = float(input("Enter your annual income: "))

# Check if the customer qualifies for a loan
if age >= 21 and income >= 21000:
    print("Congratulations, you qualify for a loan!")
else:
    print("Unfortunately, we're unable to give you a loan at this time.")