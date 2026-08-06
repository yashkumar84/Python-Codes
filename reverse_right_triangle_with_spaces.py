num = 5

for row in range(1 , num + 1):
    for star in range(num - row):
        print(" ", end=" ")
    for star in range(row):
        print("*" , end=" ")
    print()