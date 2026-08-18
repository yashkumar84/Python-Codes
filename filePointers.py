with open('text.txt' , 'r') as file:
    print(file.read(5))
    print(file.tell())
    file.seek(1)
    print(file.read(2))
    
try:
    with open('text.txt' , "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File Not Found")