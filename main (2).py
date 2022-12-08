#1. Написати програму, яка конвертує градуси у радіани
degrees = 40
pi = 3.1415926535
radians = (degrees*pi)/180
print(round(radians, 5))

#2. Написати програму, що рахує абонплату за комунальним лічильника
previous_indication = 86.56867
current_indication = 96.47756
tariff = 6.453465
total_sum = (current_indication-previous_indication)*tariff
print(round(total_sum, 2))

#3. Написати програму, що рахує податок від надхождення на рахунок підприємця.
full_amount = 100.6754
percentage = 3.5645
tax_income = (percentage*full_amount)/100
net_income = full_amount-tax_income
print(round(tax_income, 2))
print(round(net_income, 2))

#4. Написати програму що рахує витрати на паливо.
consumption_per100_km = 5.5
price_for1_liter = 34.98
user_choice = float(input("Choose how many kilometers you will be driving?"))
price = (user_choice*consumption_per100_km)/100*price_for1_liter
print(price)