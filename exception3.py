def ask():
    while True:
        try:
            n=int(input('Input an integer: '))
        except:
            print('An error occured! Please try again!')
            continue
        else:
            break
    print('Thank you, your number squared is:',n**2)
ask()