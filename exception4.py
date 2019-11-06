def checkgrade():
    while True:
        try:
            marks = int(input("enter the marks of a student = "))
            if (marks <= 100):
                print("less than 100")
        except:
            print('Enter in numbers')
            marks = int(input('enter the marks in Numbers'))
        finally:
            if (marks >= 100):
                print('enter the marks less than or equal to 100')
            if (marks >= 90 and marks <= 100):
                print('A')
            elif (marks >= 80 and marks <= 90):
                print('B')

checkgrade()












