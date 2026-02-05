raw_age = "22"
print(type(raw_age))  # <class 'str'>

age = int(raw_age)
print(type(age))  # <class 'int'>

age = 22
print(type(age))  # <class 'int'>

string_age = str(age)
print(type(string_age))  # <class 'str'>

f = 3.14  # the type is float
print(type(f))  # <class 'float'>

s = str(f)  # converting float to string
print(type(s))  # <class 'str'>

i = int(f)  # while converting a float value to an integer its fractional part is discarded
print(i)  # 3
print(type(i))  # <class 'int'>

f = float(i)
print(f)  # 3.0
print(type(f))  # <class 'float'>