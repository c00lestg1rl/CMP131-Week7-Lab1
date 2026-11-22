# Samantha Vasquez
# CMP131: Week 7,Lab 1
# Program 2: Calories Burned 
# October 29, 2026

# Part 1: Create the Required Variables
print(f'~~~ Program for Calculating Calories Burned ~~~')
calories_per_min= 3.6

print('MINUTES\tCALORIES BURNED')
print('----------')

for minutes in range(5, 31, 5):
    calories_burned= minutes * calories_per_min
    print(minutes," ", calories_burned)
