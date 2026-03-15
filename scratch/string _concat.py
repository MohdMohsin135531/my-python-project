# Variables in python
name = "John"      # String variable
age = 20           # Integer variable
gpa = 3.9          # Float variable
is_student = True  # Boolean variable

# Prints all the data in string format
print("Name: " + name)
print("Age: " + str(age))
print("GPA: " + str(gpa))
print("Is student: " + str(is_student))

# example 1
print("You're doing great!")  #Use double quotes if your string contains single quotes.
print('You\'re doing great!')
# example 2
print("Have you read \"Hamlet\"?")  #However, it's considered best practice to avoid backslashes inside the strings – even though it works.
print('Have you read "Hamlet"?')  # Use single quotes if your string contains double quotes.

# Multiline strings
print("""This
is
a
multi-line
string""")  # To print multi-line string use triple quotes on each side of the string literal.

print('''This
is
a
multi-line
string''')  # Again, the choice of single or double quotes is up to you as both work fine in Python.