abs_integer = abs(-10)  # 10
abs_float = abs(-10.0)  # 10.0

round_integer = round(10.0)      # 10, returns integer when ndigits is omitted
round_float = round(10.2573, 2)  # 10.26

pow_integer = pow(2, 10)  # 1024
pow_float = pow(2.0, 10)  # 1024.0

largest = max(1, 2, 3, 4, 5)   # 5
smallest = min(1, 2, 3, 4, 5)  #    1

# abs() and pow() functions have equivalents in the math module. The key difference of math.fabs() and math.pow() is that they always return floats: 
import math # importing math module

fabs_integer = math.fabs(-10)  # 10.0
fabs_float = math.fabs(-10.0)  # 10.0

pow_integer = math.pow(2, 10)  # 1024.0
pow_float = math.pow(2.0, 10)  # 1024.0

# Suppose you raised x to the power y, and then forgot y. You can recover it using the math.log() function:
x = 2
y = 10
pow = math.pow(x, y)    # 1024.0
log = math.log(pow, x)  # 10.0

# math.log(pow, x) returns z such that x raised to the power z equals pow. If the second argument x (called the base of the logarithm) is omitted, it is considered equal to a special number e (approximately 2.718):

natural_log = math.log(1024)  # 6.931471805599453 

floor = math.floor(6.931471805599453)  # 6
ceil = math.ceil(6.391471805599453)    # 7

result = math.sqrt(100)  # 10.0
print(result)    

r = 3.5
circumference = 2 * math.pi * r  # 21.991...

deg = 60.0
x = math.radians(deg)  # 1.047...

cos = math.cos(x)  # 0.500...
sin = math.sin(x)  # 0.866...

degrees = math.degrees(x)  # 59.999...

# This is how we can calculate the volume using Python:
deg = 60.0
x = math.radians(deg)  # 1.047...

cos = math.cos(x)  # 0.500...
sin = math.sin(x)  # 0.866...

degrees = math.degrees(x)  # 59.999...