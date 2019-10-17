a=input("enter the character : ")

def check_vowel(a):
    vowel = 'AaEeiIoOuU'

    if a in vowel:
        print(f"{a} is a vowel")
    else:
        print(f"{a} is a consonant")

check_vowel(a)