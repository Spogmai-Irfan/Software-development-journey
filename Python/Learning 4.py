#Break and Continue Programs
#Example 1
correct_password = "Spogmai123"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login Successful")
        break
    print("Wrong Password")

#Example 2
secret = 7
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct")
        break
    print("Wrong")

#Example 3
for i in range(1, 11):
    if i == 5:
        break
    print(i)

#Example 4
for i in range(1, 11):
    if i == 5:
        continue
    print(i)   

 #Example 5
    numbers = [10, -2, 15, -8, 20, -1]
for num in numbers:
    if num < 0:
        continue
    print(num) 

 #Example 6
    for i in range(5):
       name = input("Enter your name: ")
    if name == "":
        continue
    print("Salam", name)   

       