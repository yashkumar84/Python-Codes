marks = int(input("ENTER THE MARKS"))

# marks >= 90 - A Grade 
# marks >= 80 - B Grade 
# marks >= 70 - C Grade
# marks >= 60 - D Grade
# marks < 60 - Fail

if marks >= 90:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 70:
    print("C Grade")
elif marks >= 60:
    print("D Grade")
else:
    print("Fail")
