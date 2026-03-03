n = int(input())
fd = n // 100
sd = n // 10 % 10
ld = n % 10
print(fd + sd + ld)

# Another way
print(sum(int(x) for x in input()))