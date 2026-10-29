# Samantha Vasquez
# CMP131: Week 7, lab 1
# Program 1: Fast freight Shipping Charges 
# October 29, 2026

# Part 1: Displaying a Program Title 
print(f'~~~Fast Freight Shipping Charges Calculator~~~')

# Part 2: Package Weight Input
package_weight= float(input('Enter the package weight in kilograms: '))
while package_weight <= 0 or package_weight > 20:
    print('Error: weight is invalid.')
    package_weight= float(input('Enter a valid value for the weight: '))
print(f'The package weight you entered is: {package_weight}')

# Part 3: Shipping Distance Input
shipping_distance= int(input('Enter the shipping distance in miles: '))
while shipping_distance <= 10 or shipping_distance > 3000:
    print('Error: shipping distance is invalid.')
    shipping_distance= int(input('Enter a vlalid value for the shipping distance: '))
print(f'The shipping distance you entered is: {shipping_distance}')

# Part 4: Determine the Shipping Rate 
if package_weight <= 2:
    rate= 1.10
elif package_weight >= 2 and package_weight <= 6:
    rate= 2.20
elif package_weight >= 6 and package_weight <= 10:
    rate= 3.70
elif package_weight >= 10 and package_weight <= 20:
    rate= 4.80
print(f'The rate per 500 miles is:  ${rate: .2f}')

# Part 5: Calculate the Shipping Charge
shipping_charge= rate * (shipping_distance/500)
print(f'The total shipping charge for this package is: ${shipping_charge: .2f}')