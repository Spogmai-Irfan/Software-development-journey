#List 
#Example 1
# List of student marks
marks = [78, 85, 90, 67, 88]
print("Student Marks:", marks)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Total Marks:", sum(marks))
print("Average Marks:", sum(marks) / len(marks))
marks.append(95)
print(" Marks:", marks)
marks.sort()
print("Marks:", marks)

#Example 2
shopping = ["Milk", "Bread", "Eggs", "Rice"]
print("Shopping List:", shopping)
shopping.append("Butter")
print("Shopping:", shopping)
shopping.remove("Bread")
print("Shopping:", shopping)
print("Length:", len(shopping))
shopping.sort()
print(" Shopping:", shopping)

# Example 3
temperatures = [32, 34, 31, 35, 33, 30, 36]
print("Temperatures:", temperatures)
print("Highest Temperature:", max(temperatures))
print("Lowest Temperature:", min(temperatures))
print("Average Temperature:", sum(temperatures) / len(temperatures))
temperatures.reverse()
print("Reversed List:", temperatures)

#Tuples programs code
#Example 1
student = ("Spogmai", 20, "Computer Software Engineering", "A")
print("Student Name:", student[0])
print("Age:", student[1])
print("Department:", student[2])
print("Grade:", student[3])
print("Total Elements:", len(student))

#Example 2
sales = (1200, 1500, 1800, 1700, 2000, 2200)
print("Monthly Sales:", sales)
print("Highest Sale:", max(sales))
print("Lowest Sale:", min(sales))
print("Total Sales:", sum(sales))
print("Average Sales:", sum(sales) / len(sales))

#Example 3
subjects = ("English", "Math", "Physics", "Chemistry", "Math")
print("Subjects:", subjects)
print(" Subject:", subjects[0])
print(" Subject:", subjects[-1])
print("Math appears", subjects.count("Math"), "times")
print("Physics:", subjects.index("Physics"))
print("Total Subjects:", len(subjects))

#Sets 
#Example 1
subjects = {"Math", "English", "Physics", "Computer"}
print("Original Subjects:", subjects)
subjects.add("Chemistry")
print("Subjects:", subjects)
subjects.remove("English")
print("Subjects:", subjects)
if "Math" in subjects:
    print("Math is present in subjects")
else:
    print("Math is not present in subjects")
print("Total Subjects:", len(subjects))

#Example 2
group_A = {"Cricket", "Football", "Hockey", "Tennis"}
group_B = {"Football", "Basketball", "Cricket", "Volleyball"}
print("Group A:", group_A)
print("Group B:", group_B)
print("Sports:", group_A.union(group_B))
print("Sports:", group_A.intersection(group_B))
print("Sports:", group_A.difference(group_B))
print("Sports:", group_B.difference(group_A))

#Example 3
fruits = {"Apple", "Banana", "Mango", "Orange"}
print("Original Fruits:", fruits)
fruits.add("Grapes")
fruits.add("Pineapple")
print(" Fruits:", fruits)
fruits.discard("Banana")
print("Fruits:", fruits)
if "Mango" in fruits:
    print("Mango is present")
else:
    print("Mango is not present")
print(" Fruits:", len(fruits))
fruits.clear()
print("Fruits:", fruits)