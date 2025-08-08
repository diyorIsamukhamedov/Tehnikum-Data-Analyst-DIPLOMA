######################################################################################################
small_bottle_price = 0.10 # Price of a small bottle (in dollars)
large_bottle_price = 0.25 # Price of a large bottle (in dollars)

# Asking the user for the quantity of bottles of each size
small_bottles_quantity = int(input("Enter the number of bottles (1 liter or less): "))
large_bottles_quantity = int(input("Enter the number of bottles (more than 1 liter): "))

# Calculating the sum
sum_of_all_bottles = (small_bottles_quantity * small_bottle_price) + (large_bottles_quantity * large_bottle_price)

# Displaying the calculation of a sum
print(f"{sum_of_all_bottles}$")
######################################################################################################

# Prompting the user to enter the total order amount in the restaurant
order_sum = float(input("Enter the total amount for your restaurant order: "))

# Defining tax rates
vat_rate = 0.12 # VAT rate in Uzbekistan (12%)
service_tax = 0.18 # Service tax rate in the restaurant (tip for the waiter)

# Calculating VAT and service tax based on the order amount
calc_vat_rate = vat_rate * order_sum
calc_service_tax = service_tax * order_sum

# Calculating the final amount including VAT and service tax
total_amount = order_sum + calc_vat_rate + calc_service_tax

# Displaying calculated tax amounts and the final bill
print(f"VAT: {calc_vat_rate}") # Output VAT amount
print(f"service tax: {calc_service_tax}") # Output service tax amount
print(f"total amount: {total_amount}") # Output total amount including taxes
######################################################################################################

# Prompting the user to enter the natural number
n = int(input("Enter a number to calculate natural numbers from 1 to your input: "))

# Calculating the sum using the formula
sum_natural = (n * (n + 1)) // 2 # Integer division for accuracy

# Printing the result
print(f"The sum of the first {n} positive numbers is: {sum_natural}")
######################################################################################################

# Prompting the user to enter the souvenir and trinket quanty
souvenir_quantity = int(input("Enter the quantity of souvenirs to calculate the total weight: "))
trinket_quantity = int(input("Enter the quantity of trinkets to calculate the total weight: "))

# Souvenir and trinket weight
souvenir_weight = 75
trinket_weight = 112

# Calculating total weight
total_weight = (souvenir_quantity * souvenir_weight) + (trinket_quantity * trinket_weight)

# Printing the result
print(f"The total weight is: {total_weight}g")
######################################################################################################