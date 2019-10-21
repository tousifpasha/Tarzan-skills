d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key_exists():
   for i in d:
        x=int(input("enter the key to check it exists or not : "))
        if x in d:
            print("key already exists")
        else:
            print("key doesnot exists")
key_exists()



