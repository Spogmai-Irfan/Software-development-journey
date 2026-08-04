#Loops
#Example 1
total = 0
for i in range(1, 6):
    total += i
print("Sum =", total)

#Example 2
balance = 1000
while balance > 0:
    print("Current Balance:", balance)
    withdraw = int(input("Enter amount to withdraw: "))
    balance -= withdraw
print("Balance is zero or below")

#Example 3
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

 #Example 4
num_students = int(input("Enter number of students: "))

total_marks = 0
highest = 0
lowest = 100

for i in range(1, num_students + 1):
    print("\nStudent", i)

    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    total_marks += marks

    if marks > highest:
        highest = marks
        topper = name

    if marks < lowest:
        lowest = marks
        low_student = name

average = total_marks / num_students
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Topper:", topper)
print("Lowest Marks:", lowest)
print("Lowest Scorer:", low_student)

#Example 5
secret = 15
attempts = 0
while True:
    guess = int(input("Guess the number (1-20): "))
    attempts += 1
    if guess == secret:
        print("Congratulations")
        print("You guessed correctly.")
        print("Attempts:", attempts)
        break
    elif guess < secret:
        print(" Low")

    else:
       print(" High")       

#Example 6
total_bill = 0

while True:

    item = input("\nEnter item name: ")
    price = float(input("Enter item price: "))

    total_bill += price

    choice = input("Add another item(yes,no) ")

    if choice.lower() <= "yes":
        break
print("Total Amount =", total_bill)
discount = 0
if total_bill >= 5000:
    discount = total_bill * 0.20

elif total_bill >= 3000:
    discount = total_bill * 0.10

elif total_bill >= 1000:
    discount = total_bill * 0.05

final_bill = total_bill - discount

print("Discount =", discount)
print("Final Bill =", final_bill)

#Example 7
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):

    print("\nMultiplication Table of", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)