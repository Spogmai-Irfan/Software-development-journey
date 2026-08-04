#  Datatype and Variables in Python
#Example 1
age = 20
height = 5.8
name = "Spogmai"
is_student = True
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

#Example 2
city = "Mardan"
temperature = 32.5
population = 500000
is_raining = False
print("city:",type(city))
print("temperature:", type(temperature))
print("population:", type(population))
print("is_raining:", type(is_raining))

#Example 3
integer_num = 100
float_num = 99.99
string_text = "Python Programming"
boolean_value = True
list_data = [10, 20, 30]
tuple_data = (1, 2, 3)
dictionary_data = {"name": "Ali", "age": 22}

print("Integer:", integer_num)
print("Float:", float_num)
print("String:", string_text)
print("Boolean:", boolean_value)
print("List:", list_data)
print("Tuple:", tuple_data)
print("Dictionary:", dictionary_data)

# Strings
#Example 1
a = "Spogmai"
b = "Irfan"

print(a)
print(b)
#Example 2
first = "My name is spogmai."
second = "I'm learning Phyton"

message = first + " " + second
print(message)
#Example 3
word = "Spogmai Irfan"
print(len(word))

#Example 4
text = "Spogmai"
print(text[0])   
print(text[2])  

#Example 5
name = "Ayeshooo"
print(name.upper())
print(name.lower())

#Example 6
sentence = "I like cats"
new_sentence = sentence.replace("cats", "dogs")
print(new_sentence)

 #Example 7
text = "Talhooo"
print(text[0:3])
print(text[2:])

#Example 8
name = "Spogmai"
age = 21
print(f"My name is {name} and I am {age} years old.")
