#Dictionary programs
#Exampple 1
students = {
    101: {"name": "Ali", "age": 20, "marks": 88},
    102: {"name": "Sara", "age": 21, "marks": 91},
    103: {"name": "Ahmed", "age": 19, "marks": 76}
}
for roll, info in students.items():
    print("Roll Number:", roll)
    print("Name:", info["name"])
    print("Age:", info["age"])
    print("Marks:", info["marks"])
    print()
highest_marks = 0
top_student = ""
for info in students.values():
    if info["marks"] > highest_marks:
        highest_marks = info["marks"]
        top_student = info["name"]
print("Students:", top_student)
print(" Marks:", highest_marks)
students[104] = {"name": "Fatima", "age": 22, "marks": 95}
print(" Students")
for roll, info in students.items():
    print(roll, info)

 #Example 2
    cart = {
    "Rice": {"price": 250, "quantity": 2},
    "Sugar": {"price": 180, "quantity": 3},
    "Milk": {"price": 220, "quantity": 4},
    "Eggs": {"price": 350, "quantity": 1}
}
grand_total = 0
for item, details in cart.items():
    total = details["price"] * details["quantity"]
    print("Item:", item)
    print("Price:", details["price"])
    print("Quantity:", details["quantity"])
    print("Total:", total)
    grand_total += total
print("Total =", grand_total)
cart["Bread"] = {"price": 150, "quantity": 2}
print("Cart")
for item in cart:
    print(item, cart[item])  

#File Handling programs
#Example 1
file = open("students.txt", "w")
file.write("Ali - 85\n")
file.write("Sara - 92\n")
file.write("Ahmed - 78\n")
file.write("Fatima - 90\n")
file.close()
file = open("students.txt", "r")
print("Student Records")
content = file.read()
print(content)
file.close()

#Example 2
file = open("employees.txt", "w")
employees = [
    ["Spogmai", "IT", 85000],
    ["Talhooo", "HR", 60000],
    ["Irfan", "Finance", 75000],
    ["Sumbul", "Marketing", 70000]
]
for employee in employees:
    line = employee[0] + ", " + employee[1] + ", " + str(employee[2]) + "\n"
    file.write(line)
file.close()
file = open("employees.txt", "r")
print("Employee Records")
for line in file:
    data = line.strip().split(", ")
    print("Name:", data[0])
    print("Department:", data[1])
    print("Salary:", data[2])
    print()
file.close()
     