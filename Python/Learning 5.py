#List programs
#Example 1
marks = [78, 85, 90, 67, 88]
print("Student Marks:", marks)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Total Marks:", sum(marks))
print("Average Marks:", sum(marks) / len(marks))
marks.append(95)
print("Marks:", marks)
marks.sort()
print("Marks:", marks)

#Example 2
shopping = ["Milk", "Bread", "Eggs", "Rice"]
print("Shopping:", shopping)
shopping.append("Butter")
print("Shopping:", shopping)
shopping.remove("Bread")
print("Shopping:", shopping)
print("Length:", len(shopping))
shopping.sort()
print("Shopping :", shopping)

#Tuple programs
#Example 1
student = ("Spogmai", 20, "Computer SoftwareEngineering", "A")
print("Student Name:", student[0])
print("Age:", student[1])
print("Department:", student[2])
print("Grade:", student[3])
print("Length:", len(student))

#Example 2
subjects = ("English", "Math", "Physics", "Chemistry", "Math")
print("Subjects:", subjects)
print(" Subject:", subjects[0])
print(" Subject:", subjects[-1])
print("Math", subjects.count("Math"), "times")
print(" Physics:", subjects.index("Physics"))
print("Length:", len(subjects))

#Sets Programs
#Example 1
subjects = {"Math", "English", "Physics", "Computer"}
print("Subjects:", subjects)
subjects.add("Chemistry")
print(" Subjects:", subjects)
subjects.remove("English")
print("Subjects:", subjects)
if "Math" in subjects:
    print("Math is present")
else:
    print("Math is not present")
print("Total Subjects:", len(subjects))

#Example 2
fruits = {"Apple", "Banana", "Mango", "Orange"}
print("Original Fruits:", fruits)
fruits.add("Grapes")
fruits.add("Pineapple")
print(" Fruits:", fruits)
fruits.discard("Banana")
print("Fruits:", fruits)
if "Mango" in fruits:
    print("Mango is available.")
else:
    print("Mango is not available.")
print("Number of Fruits:", len(fruits))
fruits.clear()
print("Fruits :", fruits)
