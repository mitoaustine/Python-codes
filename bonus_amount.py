# Prompt the user for their salary and years of service
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

# Calculate the bonus based on the years of service
if years_of_service > 10:
    bonus_percent = 0.10
elif years_of_service >= 6 and years_of_service <= 10:
    bonus_percent = 0.08
else:
    bonus_percent = 0.05

bonus_amount = salary * bonus_percent

# Print the net bonus amount
print(f"Your bonus amount is: {bonus_amount:.2f}")