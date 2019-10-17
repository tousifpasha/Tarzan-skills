n=int(input("enter the number : "))
fact = 0
def fact(n):
    if n == 0:
        return 1
    else:

      return n* fact(n-1)
print(f"factorial of {n} is {fact(n)}")
#print(fact(n))