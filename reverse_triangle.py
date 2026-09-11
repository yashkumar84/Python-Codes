nums = 5
for row in range (nums):
    for star in range(nums - row):
        print("*", end=" ")
    
    print()