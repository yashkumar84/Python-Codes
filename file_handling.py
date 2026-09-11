# file = open('text.txt' , 'r')

# r - read , w - write , a - append , x - create new File , r+ - read + write , w+ - write + read  , a+ - append + read

# data = file.read()
# print(data)

# file.close()

with open('text.txt' , 'r') as file:
    data = file.readlines()
    print(data)
    

