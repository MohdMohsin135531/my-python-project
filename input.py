age = input("How old are you? ") # Returns string; use int(age) for calculations
print("I know, that you're " + age + " years old") # String concatenation with +
print('I am also ' + age + " years old") # Single/double quotes work the same

# Another way to do this is to print the message separately:
print("How old are you?")
age = input()
print("I know, that you're " + age + " years old")

# If you want an input to be a number, you should write it explicitly:
print("What's your favorite number?")
value = int(input())  # now value keeps an integer number