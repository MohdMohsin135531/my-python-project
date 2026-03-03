# Variable takes the value of the next item from the iterable after each iteration.
iterable = [1, 2, 3]
for variable in iterable:
    print(variable)

oceans = ['Atlantic', 'Pacific', 'Indian', 'Southern', 'Arctic']
for ocean in oceans:
    print(ocean)

for char in 'magic':
    print(char)

# Last number won't be in the output since we started from 0.
for i in range(5):  # range function 
    print(i)

# You can configure the increment (step) value by adding a third parameter
for i in range(5, 45, 10):
    print(i)

# In the example above, we don't need the counter variable in any way, we simply use the loop to repeat the do_smth() function a given number of times.
def do_smth():
    pass

for _ in range(100):
    do_smth()
    
# Input data processing
times = int(input('How many times should I say "Hello"?'))
for i in range(times):
    print('Hello!')

# Printing 1 to 10
print("1 2 3 4 5 6 7 8 9 10")  # hardcoded
print(*range(1, 11))  # * unpacks the range object into separate arguments
