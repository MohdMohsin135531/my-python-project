a = int(input())
b = int(input())
count = 0
total = 0
for i in range(a, b+1):
    if i % 3 == 0:
        count += 1
        total += i
print(total / count)

# Another way to do this 
# Modulo divided by negative number behaves differently in Python
a  = int(input())
b = int(input())

a = a - (a % -3)  # first number which is multiple of 3 
r = range(a, b + 1, 3)
print(sum(r) / len(r))  