for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Another clever way to do this 
print("Other way to do this")
for i in range(1, 101): 
    print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i))
    