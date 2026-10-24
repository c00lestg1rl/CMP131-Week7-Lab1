# CMP 131 – Python Programming


> **Required file location:** Keep every Python file directly in the repository root. Do not create a `src` folder.

## Week 7 – Lab 1: Shipping Charges and Loop Applications

**Total Points: 100**

* Program 1: Fast Freight Shipping Charges — 40 points
* Program 2: Calories Burned — 30 points
* Program 3: Sum of Numbers — 30 points

## Learning Objectives

After completing this lab, students should be able to:

* Accept numeric input from the user.
* Convert input to the appropriate numeric data type.
* Validate input using conditional statements and loops.
* Use `if`, `elif`, and `else` statements to select a rate.
* Use loops to repeat calculations.
* Use an accumulator variable to calculate a running total.
* Work with loop starting values, ending values, and increments.
* Format monetary and numeric output.
* Test programs using normal, boundary, and invalid values.
* Use comments to explain the major sections of a program.

## Assignment Overview

Create three separate Python programs.

The first program calculates shipping charges based on package weight and shipping distance.

The second program uses a loop to display the calories burned after specific amounts of time on a treadmill.

The third program uses a loop and an accumulator to calculate the sum of all integers from `1` through a positive integer entered by the user.

Create the following Python files:

* `shipping_charges.py`
* `calories_burned.py`
* `sum_of_numbers.py`

The instructor is not providing completed Python code or an exact output design. Students must design, write, and test their own programs.

# Program 1: Fast Freight Shipping Charges

**Points: 40**

## Program Description

The Fast Freight Shipping Company calculates shipping charges based on the weight of a package and the distance it will be shipped.

Use the following shipping rates:

| Weight of Package                                | Rate per 500 Miles |
| ------------------------------------------------ | -----------------: |
| 2 kilograms or less                              |              $1.10 |
| Over 2 kilograms but not more than 6 kilograms   |              $2.20 |
| Over 6 kilograms but not more than 10 kilograms  |              $3.70 |
| Over 10 kilograms but not more than 20 kilograms |              $4.80 |

Create a program that asks the user for:

* The weight of the package in kilograms
* The shipping distance in miles

The program must determine the correct shipping rate, calculate the shipping charge, and display a complete shipping summary.

## Required Python File

Create a Python file named:

`shipping_charges.py`

Include a comment header containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: Display a Program Title

Display a descriptive title when the program begins.

The title should clearly indicate that the program calculates Fast Freight shipping charges.

Students should create their own title and output design.

## Part 2: Package Weight Input

Ask the user to enter the package weight in kilograms.

The weight may contain a decimal value.

Convert the input to an appropriate numeric data type and store it in a meaningfully named variable.

The company accepts only packages that weigh:

* More than `0` kilograms
* No more than `20` kilograms

Use a loop to continue asking for the weight until the user enters a valid value.

Display an appropriate error message whenever the weight is invalid.

## Part 3: Shipping Distance Input

Ask the user to enter the shipping distance in miles.

The distance may be entered as a whole number.

The company accepts shipping distances from:

* A minimum of `10` miles
* A maximum of `3,000` miles

Use a loop to continue asking for the distance until the user enters a valid value.

Display an appropriate error message whenever the distance is:

* Less than `10` miles
* Greater than `3,000` miles

## Part 4: Determine the Shipping Rate

Use an `if`, `elif`, and `else` structure to determine the correct rate.

Apply the following rules:

* A package weighing `2` kilograms or less uses the `$1.10` rate.
* A package weighing more than `2` kilograms but no more than `6` kilograms uses the `$2.20` rate.
* A package weighing more than `6` kilograms but no more than `10` kilograms uses the `$3.70` rate.
* A package weighing more than `10` kilograms but no more than `20` kilograms uses the `$4.80` rate.

Every valid package must be assigned exactly one shipping rate.

## Part 5: Calculate the Shipping Charge

The selected rate applies to every 500 miles shipped.

Use the following calculation:

**Shipping charge = Rate × (Shipping distance ÷ 500)**

Store the calculated shipping charge in a meaningfully named variable.

## Part 6: Display the Shipping Summary

Display a clearly formatted shipping summary containing:

* Package weight
* Shipping distance
* Rate per 500 miles
* Total shipping charge

All monetary values must:

* Include a dollar sign.
* Display exactly two digits after the decimal point.
* Include clear labels.

## Required Testing for Program 1

### Test 1: First Weight Range

* Package weight: `2`
* Shipping distance: `500`
* Rate: `$1.10`
* Shipping charge: `$1.10`

### Test 2: Second Weight Range

* Package weight: `4`
* Shipping distance: `1000`
* Rate: `$2.20`
* Shipping charge: `$4.40`

### Test 3: Third Weight Range

* Package weight: `8`
* Shipping distance: `1500`
* Rate: `$3.70`
* Shipping charge: `$11.10`

### Test 4: Fourth Weight Range

* Package weight: `15`
* Shipping distance: `2000`
* Rate: `$4.80`
* Shipping charge: `$19.20`

### Test 5: Invalid Weight

First enter:

`0`

The program must display an error message and ask for the weight again.

Then enter:

`5`

The program must accept the new value and continue.

### Test 6: Weight Above Maximum

First enter:

`21`

The program must display an error message and ask for the weight again.

### Test 7: Invalid Distance

First enter:

`9`

The program must display an error message and ask for the distance again.

### Test 88: Distance Above Maximum

First enter:

`3001`

The program must display an error message and ask for the distance again.

## Program 1 Point Distribution

* Program title and clear input prompts: 4 points
* Correct input conversion: 4 points
* Weight validation loop: 6 points
* Distance validation loop: 6 points
* Correct shipping-rate conditions: 8 points
* Correct shipping-charge calculation: 5 points
* Clear monetary formatting and output: 4 points
* Comment header, code comments, and testing: 3 points

**Program 1 Total: 40 points**

# Program 2: Calories Burned

**Points: 30**

## Program Description

Running on a particular treadmill burns approximately **3.6 calories per minute**.

Create a program that uses a loop to display the number of calories burned after:

* 5 minutes
* 10 minutes
* 15 minutes
* 20 minutes
* 25 minutes
* 30 minutes

The program must calculate and display each result from inside the loop.

## Required Python File

Create a Python file named:

`calories_burned.py`

Include a comment header containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: Create the Required Variables

Create meaningfully named variables for:

* Calories burned per minute
* Current number of minutes
* Calories burned

Use `3.6` as the number of calories burned per minute.

## Part 2: Create the Loop

Use a loop that processes the following minute values:

`5, 10, 15, 20, 25, 30`

The loop should:

* Begin with 5 minutes.
* End with 30 minutes.
* Increase the number of minutes by 5 during each repetition.
* Calculate the number of calories burned.
* Display the result during each repetition.

Do not write six separate calculation statements. The calculations must be performed using a loop.

## Part 3: Calculate the Calories Burned

For each loop repetition, use the following calculation:

**Calories burned = Minutes × 3.6**

## Part 4: Display the Results

Display the results using clear column headings or descriptive labels.

The output must show:

* Number of minutes
* Calories burned

The results should be easy to read and consistently formatted.

## Required Testing for Program 2

The program should produce the following results:

| Minutes | Calories Burned |
| ------: | --------------: |
|       5 |            18.0 |
|      10 |            36.0 |
|      15 |            54.0 |
|      20 |            72.0 |
|      25 |            90.0 |
|      30 |           108.0 |

Confirm that:

* The loop repeats six times.
* The minute value increases by 5 each time.
* Every calculation is correct.
* The results are displayed from inside the loop.
* The program runs without errors.

## Program 2 Point Distribution

* Program title and required variables: 5 points
* Correct loop starting value: 5 points
* Correct loop ending value: 5 points
* Correct increment of 5 minutes: 5 points
* Correct calorie calculation: 5 points
* Clear output, comments, and successful testing: 5 points

**Program 2 Total: 30 points**

# Program 3: Sum of Numbers

**Points: 30**

## Program Description

Create a program that asks the user to enter a positive integer.

The program must use a loop to calculate the sum of all integers from `1` through the number entered.

For example, if the user enters `5`, the program calculates:

**1 + 2 + 3 + 4 + 5 = 15**

If the user enters `50`, the program calculates the sum of:

**1 + 2 + 3 + 4 + … + 50**

The program must use a loop and an accumulator variable. Do not use Python’s built-in `sum()` function.

## Required Python File

Create a Python file named:

`sum_of_numbers.py`

Include a comment header containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: User Input

Ask the user to enter a positive integer.

Convert the input to the integer data type and store it in a meaningfully named variable.

A positive integer must be greater than zero.

Examples of valid values include:

* `1`
* `5`
* `10`
* `50`

## Part 2: Input Validation

Do not accept zero or a negative starting number.

Use a loop to continue asking for an integer until the user enters a value greater than zero.

For every invalid value:

* Display an appropriate error message.
* Ask the user to enter another value.
* Do not perform the summation until the value is valid.

## Part 3: Create an Accumulator

Create an accumulator variable before the loop that performs the summation.

The accumulator must begin at `0`.

During each repetition, add the current integer to the accumulator.

## Part 4: Calculate the Sum

Use a loop to process every integer beginning with `1` and ending with the number entered by the user.

For example, if the user enters `5`, the loop processes:

`1, 2, 3, 4, 5`

The ending number must be included in the calculation.

Do not manually write each addition, and do not use the built-in `sum()` function.

## Part 5: Display the Result

After the loop finishes, display:

* The positive integer entered by the user
* The calculated sum from `1` through that integer

Use a complete and clearly formatted message.

## Required Testing for Program 3

### Test 1

* Number entered: `1`
* Expected sum: `1`

### Test 2

* Number entered: `5`
* Expected sum: `15`

### Test 3

* Number entered: `10`
* Expected sum: `55`

### Test 4

* Number entered: `50`
* Expected sum: `1275`

### Test 5: Invalid Negative Value

First enter:

`-5`

The program must display an error message and ask for another number.

Then enter:

`5`

The program must accept the new number and display a sum of `15`.

### Test 6: Invalid Zero

First enter:

`0`

The program must display an error message and ask for another number.

Confirm that:

* Invalid values are not accepted.
* The input-validation loop works correctly.
* The summation begins with `1`.
* The number entered by the user is included.
* The accumulator contains the correct final total.
* The program runs without errors.

## Program 3 Point Distribution

* Program title and clear input prompt: 4 points
* Correct integer conversion: 4 points
* Correct input-validation loop: 6 points
* Correct accumulator initialization: 4 points
* Correct summation loop: 6 points
* Correct final result: 3 points
* Clear output, comments, and successful testing: 3 points

**Program 3 Total: 30 points**

# Code Comments

Use comments to identify and explain the major sections of all three programs.

Include comments for:

* The program information header
* The program title
* Variable initialization
* User input
* Input validation
* Conditional statements
* Loop processing
* Calculations
* Final output

Comments should briefly explain the purpose of each major section. They do not need to repeat every Python statement.

# Functional Requirements

## Fast Freight Shipping Program

When `shipping_charges.py` runs, it must:

* Display a descriptive program title.
* Ask for the package weight.
* Accept package weights greater than 0 and no more than 20 kilograms.
* Reject invalid weights and ask again.
* Ask for the shipping distance.
* Accept distances from 10 through 3,000 miles.
* Reject invalid distances and ask again.
* Use conditional statements to determine the correct shipping rate.
* Calculate the shipping charge.
* Display a complete shipping summary.
* Format monetary values to two decimal places.
* Run without errors.

## Calories Burned Program

When `calories_burned.py` runs, it must:

* Use 3.6 calories per minute.
* Use a loop.
* Process minutes from 5 through 30 in increments of 5.
* Calculate the calories burned during each repetition.
* Display all six required results.
* Run without errors.

## Sum of Numbers Program

When `sum_of_numbers.py` runs, it must:

* Ask the user for a positive integer.
* Reject zero and negative integers.
* Use a loop for input validation.
* Create an accumulator beginning at zero.
* Use another loop to process the integers from 1 through the entered number.
* Include the entered number in the sum.
* Display the final sum.
* Avoid using the built-in `sum()` function.
* Run without errors.

# General Requirements

* Use Python to complete all three programs.
* Create all three required Python files.
* Use meaningful and consistent variable names.
* Convert user input to the appropriate data type.
* Use loops where required.
* Use conditional statements where required.
* Include a complete comment header in every file.
* Include comments explaining the major sections.
* Use clear input prompts, headings, and output labels.
* Format monetary values to two decimal places.
* Test each program using the required test values.
* Check spelling, capitalization, grammar, and punctuation.
* Make sure all three programs run without errors.
* Follow the course AI-use policy.
* Record any AI assistance in `AI-Use-Report.md`.

# Required Organization

Organize the assignment as follows:

* `Week-07`

  * `Lab-01`

    * `CMP131-Week-07-Lab-01.md`
    * `AI-Use-Report.md`
    * `src`

      * `shipping_charges.py`
      * `calories_burned.py`
      * `sum_of_numbers.py`

# Submission Requirements

Submit or push the complete `Lab-01` folder.

The submission must include:

* `shipping_charges.py`
* `calories_burned.py`
* `sum_of_numbers.py`
* `AI-Use-Report.md`

Before submitting, verify that:

* All three required Python files are included.
* All filenames are correct.
* Every program contains the required comment header.
* Every program includes appropriate code comments.
* The shipping program validates the package weight.
* The shipping program validates the shipping distance.
* All four shipping-rate ranges work correctly.
* The shipping charge is calculated correctly.
* The calorie program uses a loop.
* The calorie program processes the required minute values.
* The sum program validates the user’s input.
* The sum program uses an accumulator.
* The sum program includes the ending number in the calculation.
* The built-in `sum()` function is not used.
* All required test values were completed successfully.
* All programs run without errors.
* The AI-use report is complete.
* The latest work has been committed and pushed to GitHub.

# Suggested Git Commit Messages

* Create Week 7 Lab 1 Python files
* Add package weight and distance validation
* Add Fast Freight shipping rates
* Calculate and format shipping charges
* Add calories-burned loop
* Test treadmill calorie calculations
* Add sum-of-numbers accumulator
* Add positive-number validation
* Test all Week 7 programs
* Complete Week 7 Python lab

---

## GitHub Starter Repository

Use the following public starter repository:

[CMP131-Week-07-Lab-01](https://github.com/ahedhli12/CMP131-Week-07-Lab-01)

### Getting Started

1. Open the starter repository using the link above.
2. Select **Use this template → Create a new repository** when the template option is available.
3. Choose your personal GitHub account as the owner.
4. Name your repository `LastName-FirstName-CMP131-Week-07-Lab-01`.
5. Set your repository to **Public**.
6. Clone your own newly created repository—not the instructor’s starter repository.
7. Open the entire cloned folder in Visual Studio Code.
8. Complete and test every required Python file.
9. Commit and push your work to GitHub.
10. Verify that your latest files appear on GitHub.
11. Complete `AI-Use-Report.md`.
12. Submit the required work through Blackboard Ultra and include your public repository link when requested.

### Required Repository Files

- `CMP131-Week-07-Lab-01.md`
- `AI-Use-Policy.md`
- `AI-Use-Report.md`
- `calories_burned.py`
- `shipping_charges.py`
- `sum_of_numbers.py`

### Before You Submit

- [ ] All required Python files are in the repository root.
- [ ] Every required filename is exact.
- [ ] Each program runs successfully.
- [ ] Required tests and screenshots are complete.
- [ ] `AI-Use-Report.md` is complete and accurate.
- [ ] The latest commit is visible on GitHub.
