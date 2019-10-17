str1=input("enter the string : ")
def check_character():
    if str1[0] == str1[-1]:
        print("starting and ending characters are same")
    else:
        print("starting and ending characters are not same")
check_character()