# Samantha Vasquez
# CMP131: Week 7,Lab 1
# Program 3: Sum of Numbers
# October 29, 2026

# Part 1: User Input 
print(f'~~~ Sum Program ~~~')
integer= int(input('Enter any positive integer: '))

# Part 2: Input validation 
while integer <= 0: 
    print(f'ERROR: Invalid Value - Integer must be positive')
    integer= int(input('Please enter a new value: '))

#Part 3: Create an Accumulator 
total = 0 

# Part 4: Calculate the Sum 
for number in range(1, (integer+1)):
    total= total + number
print(f'You entered {integer}') 
print(f'The sum of the integer you entered is: {total}')