
print("Electricity bill estimator")
cents_per_kWh = input("Enter cents per kWh: ")
daily_use = input("Enter daily use in kWh: ")
number_of_billing_days = input("Enter number of billing days: ")
cents_per_kWh = int(cents_per_kWh) / 100
estimated_bill = float(daily_use) * int(number_of_billing_days)
estimated_bill = estimated_bill * cents_per_kWh
print("Estimated bill: " + str(estimated_bill))