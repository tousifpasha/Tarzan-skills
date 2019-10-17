numbers=(1,2,3,4,5,6,7,8,9)
evencount=0
oddcount=0
for i in numbers:
    if(i % 2 == 0):
        evencount += 1

    else:
        oddcount += 1
print(f"{evencount} are even numbers in the given list")
print(f"{oddcount} are odd numbers in the given list")