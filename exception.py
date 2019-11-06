def askint():
    try:
        val= int(input("please enter an integer: "))
    except:
        print("Looks like you did not enter an integer!")
        try:
            val=int(input("Try again-please enter an integer:"))
        except:
            print('Please this time enter correct value')
            val=int(input("Please please enter an integer:"))
    finally:
        print("Finally, I executed!")
    print(val)
askint()