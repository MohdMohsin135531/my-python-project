# Prompts for user's name and age
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))


# Defines a function that formats the message
def greeting(name, age):
    return f"Hello {name}, you are {age} years old!"


# Calls the function and prints out the formatted message
print(greeting(name, age))