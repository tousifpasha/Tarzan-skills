n=int(input("enter the n number : "))
m=int(input("enter the m number : "))
def squareeven():
    for i in range(n,m):
        if i % 2 == 0:
            print(f"{i} is even and its square is", i ** 2)
        else:
            print(f"{i} not an even number")
squareeven()
