#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?: $"))
number_of_people = int(input("How many people are to split the bill? "))
tip = float(input("What percentage tip would you like to give? "))
tip_percentage = tip/100

tip_amount = ((total_bill * tip_percentage) + total_bill) /number_of_people
tip_amount = round(tip_amount,2)

print(f"Each person should pay: ${tip_amount}")
