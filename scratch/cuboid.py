a = int(input())
b = int(input())
c = int(input())
print(4 * (a + b + c))
print(2 * (a * b + b * c + a * c))
print(a * b * c)

# Another way 
a, b, c = int(input()), int(input()), int(input())
print(4 * (a + b + c), 2 * (a * b + b * c + a * c), a * b * c, sep='\n')
