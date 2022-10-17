#Tip Calculator
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
tip = total_bill+(total_bill*tip_percentage/100)
person_count = int(input("How many people to split the bill?"))
tip_person = tip/person_count
final_amount = ("{:.2f}".format(round(tip_person, 2))) # "{:.2f}" used for 2 decimal places
print(f"Each person should pay: ${final_amount}")