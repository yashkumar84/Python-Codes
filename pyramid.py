num = 10

# for row in range(1 , num + 1):
#     for space in range(num - row):
#         print(" " , end="")
#     for star in range(2 * row - 1):
#         print("*" , end="")
#     print()

for row in range(1 , num + 1):
    for space in range(row - 1):
        print(" " , end="")
    for star in range((2 * num) - (2 *row) + 1):
        print("*" , end="")
    print()