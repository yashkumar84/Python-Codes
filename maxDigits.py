num = 62354
max = 0

while num > 0:
    digit = num % 10
    if digit > max:
        max = digit
    num //= 10

print(max)