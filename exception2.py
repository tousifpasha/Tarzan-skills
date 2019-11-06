x=int(input("enter the value of x: "))
y=int(input("enter the value of y: "))
z=0
try:
    z = x/y
except ZeroDivisionError:
    print("can't divide by zero!")
finally:
    print("All Done!")
print(z)