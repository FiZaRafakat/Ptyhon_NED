a = int(input("Print a number for a : "))
b = int(input("Enter a number for b : ")) 
c = int(input("Enter a number for c : "))

if a== b ==c :
    print("Equilateral")
else:
    if a == b or b == c or c == a :
        print("Isoceles")
    elif a+b>c and b+c>a and a+c>b:
        print("Scalene")
    else : 
        print("Invalid")