a=int(input("enter the side of the triangle : "))
b=int(input("enter the side of the triangle : "))
c=int(input("enter the side of the triangle : "))
if(a==b and b==c):
    print("Equilateral Triangle")
elif((a==b and b!=c) or (a!=b and a==c)):
    print("Isoceles traingle")
elif(a!=b and b!=c):
    print("Scalene Triangle")
else:
    print("not a triangle")