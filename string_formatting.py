name = 'John'
age = 20
print('Hi, my name is ' + name + ', I am ' + str(age) + ' years old!')  # an awkward way, considered a bad practice!

# The % operator is used to format strings. It is called the string formatting operator.
name = 'John'
age = 20
print('Hi, my name is %s, I am %i years old!' % (name, age))  # an old-fashioned way of formatting strings

# Old-style rounding of decimals
print('%.3f' % (11 / 3))  # 3.667
print('%.2f' % (11 / 3))  # 3.67

# The format() method is called on a string, and the arguments are passed to it. The curly braces {} are placeholders for the arguments.
name = 'John'
age = 20
print('Hi, my name is {}, I am {} years old!'.format(name, age))  # a more modern formatting method

print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))
# prints 'Strangers in the Night by Frank Sinatra'

print('{1} in the {0} by Frank Sinatra'.format('Strangers', 'Night'))
# prints 'Night in the Strangers by Frank Sinatra'

print('{1} in the {0} by Frank Sinatra: {1}'.format('Strangers', 'Night'))
# prints 'Night in the Strangers by Frank Sinatra: Night'

print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))
# prints 'Strangers in the Night by Frank Sinatra'

print('{1} in the {0} by Frank Sinatra'.format('Strangers', 'Night'))
# prints 'Night in the Strangers by Frank Sinatra'

print('{1} in the {0} by Frank Sinatra: {1}'.format('Strangers', 'Night'))
# prints 'Night in the Strangers by Frank Sinatra: Night'

print('{1} in the {0} by Frank Sinatra: {2}'.format('Strangers', 'Night', 'Some extra'))
# No longer throws IndexError

print('The {movie} movie at {theatre} was {adjective}!'.format(movie='Star Wars',
                                                        adjective='incredible',
                                                        theatre='BFI IMAX'))

# The f-strings are formatted strings. They are prefixed with the letter f. The variables are enclosed in curly braces {}.
name = 'John'
age = 20
print(f'Hi, my name is {name}, I am {age} years old!')  # another good approach to formatting strings

# You can also round decimals with f-strings by specifying the number of decimal places like this:
decimal_number = 291.68
print(f'Decimal number as is: {decimal_number}')
# Decimal number as is: 291.68

print(f'Decimal number rounded to 1 decimal place: {decimal_number:.1f}')  # a clean way of rounding decimals
# Decimal number rounded to 1 decimal place: 291.7
