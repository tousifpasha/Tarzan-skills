str1 = input("enter the two word string : ")
def name() :
    x = str1.split(' ')
    print(x)
    if x[0][0] == x[1][0]:
        return True
    else:
        return False
print(name())
