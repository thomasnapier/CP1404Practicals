loop = 0
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity bill estimator v2")
while loop == 0:
    tariff_choice = input("Which tariff? 11 or 31: ")
    if tariff_choice == "11":
        chosen_tariff = TARIFF_11
        loop = 1
    elif tariff_choice == "33":
        chosen_tariff = TARIFF_31
        loop = 1
    else:
        print("Invalid choice")
daily_use = input("Enter the daily use in kWH: ")
billing_days = input("Enter the number of billing days: ")
estimated_bill = float(daily_use) * int(billing_days)
estimated_bill = estimated_bill * chosen_tariff
print("Estimated bill: "+ str(estimated_bill))