#Operators
# Arithmetic Operators
#Example 1
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#Example 2
# Comparison Operators

x = 8
y = 10
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)

#Example 3
# Logical Operators
a = True
b = False
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

#Example 4
price = 250
quantity = 3
total = price * quantity
print("Price of one item:", price)
print("Quantity:", quantity)
print("Total Bill:", total)

#Example 5
marks = 75
passing_marks = 50
print("Passed:", marks >= passing_marks)

#Example 6
age = 20
has_license = True
print("Can drive:", age >= 18 and has_license)

#Conditional Statements
#Example 1
is_raining = True

if is_raining:
    print("Take an umbrella")
else:
    print("Don't take umbrella")

#Example 2
age = 10
if age < 12:
    print("You get a child discount")
else:
    print("You pay the regular ticket price")

#Example 3
light = "Green"

if light == "Green":
    print("Go")
elif light == "Yellow":
    print("Slow down")
else:
    print("Stop")

#Example 4
battery = 15
if battery < 10:
    print("Charge your phone.")
else:
    print("Don't charge your phone")

 #Example 5
marks = 80
if marks >= 50:
    print("Spogmai passed")
else:
    print("Spogmai failed")   

 #Example 6
name = input("Enter student name: ")
marks = int(input("Enter your marks (0-100): "))

print("\nStudent Name:", name)
print("Marks:", marks)

if marks >= 90:
    print("Grade: A+")
    print("Excellent work")
elif marks >= 80:
    print("Grade: A")
    print("Very Good")
elif marks >= 70:
    print("Grade: B")
    print("Good job")
elif marks >= 60:
    print("Grade: C")
    print("You passed")
elif marks >= 50:
    print("Grade: D")
    print(" barely passed")
else:
    print("Grade: F")
    print(" failed")

#Example 7
balance = 10000

print("Your Current Balance:", balance)

withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= 0:
    print(" Enter a valid amount")
elif withdraw > balance:
    print("Insufficient balance")
else:
    balance = balance - withdraw
    print("Withdrawal Successful")
    print("Amount Withdrawn:", withdraw)
    print("Remaining Balance:", balance)
