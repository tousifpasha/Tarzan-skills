str1=input("enter the string - ")
#str2="ing"
#str3="ly"
if(len(str1)>2):
    if str1[-3:] == 'ing':

        str1 = str1 + 'ly'
    else:
        str1 = str1 + 'ing'

print(str1)