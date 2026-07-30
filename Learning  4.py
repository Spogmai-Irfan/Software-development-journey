#Break and Continue programs
#Example 1
for i in range(1, 11):
    if i == 5:
        break
    print(i)

 #Example 2
    correct_password = "Spogmai123"
while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful!")
        break
    print("Wrong Password")   

    #Example 3
secret = 7
while True:
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct Guess")
        break
    print("Wrong Guess")

  #Example 4  
    numbers = [5, 8, 12, 20, 25]
search = int(input("Enter number to search: "))
for num in numbers:
    if num == search:
        print("Number Found")
        break

#Example 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

 #Example 6
numbers = [10, -2, 15, -8, 20, -1]
for num in numbers:
    if num <0:
        continue
    print(num) 

 #Example 7
for i in range(5):
     name = input("Enter your name: ")
     if name == "":
      continue
     print("Salam", name)     

#FUNCTIONS
#Example 1
def greet():
    print("Spogmai Irfan")
greet()

#Example 2
def course():
    print("I am playing game")
course()

#Example 3
def add(a, b):
    print("Sum =", a + b)
add(10, 20)

#Example 4
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student("Ali", 20)

# Return Statements
# Example 1
def multiply(a, b):
    return a * b
result = multiply(5, 4)
print("Multiplication =", result)

#Example 2
def square(num):
    return num * num
answer = square(4)
print("Square =", answer)
