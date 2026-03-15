print(10 + 10)   # 20
print(100 - 10)  # 90
print(10 * 10)   # 100
print(2 ** 3)    # 8 (2 to the power of 3
print(77 / 10)   # 7.7
print(77 // 10)  # 7
print(7 % 2)  # 1, because 7 is an odd number
print(8 % 2)  # 0, because 8 is an even number
# Divide the number by itself
print(4 % 4)     # 0
# At least one number is a float
print(11 % 6.0)  # 5.0
# The first number is less than the divisor
print(55 % 77)   # 55
# With negative numbers, it preserves the divisor sign
print(-11 % 5)   # 4
print(11 % -5)   # -4

# Integer division and modulo operator are related
x = 10
y = 3
print(x == (x // y) * y + (x % y))
# We can rewrite it to get the "formula" for modulo division:

print((x % y) == x - (x // y) * y)


