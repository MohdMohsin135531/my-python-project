string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count = 0
for char in string.lower():
    # Check if char is in vowels
    if char in vowels:
        count += 1
print(count)

# An alternative way to write the above code
string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count = 0

print(sum(vowel in vowels for vowel in string))
# for vowel in string:
#     if vowel in vowels:
#         count += 1
# print(count)