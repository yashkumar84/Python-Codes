num = 12345
totalSum = 0

while num > 0:
    digit = num % 10
    totalSum = totalSum + digit
    num //= 10  # num = num // 10

print(totalSum)