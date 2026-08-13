string = "    yAsH"
sent = "Hi My name is Yash"
print(string.lower())
print(string.upper())
print(string.capitalize())
print(string.count('A'))
print(string.endswith("H"))
print(string.startswith("y"))
print(string.isalnum())
print(string.lstrip())
list = sent.split(" ")
list.reverse()
st = " ".join(list)
print(st)
