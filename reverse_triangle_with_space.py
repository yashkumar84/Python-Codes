num = 5

for row in range(1 , num + 1):
    for space in range(row - 1):
        print(" " , end="")
    for star in range(num - row + 1):
        print("*" , end="")
    print()