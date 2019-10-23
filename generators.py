# def my_gen(x):
#     while(x>0):
#         if x%2==0:
#             yield 'Even'
#         else:
#             yield 'Odd'
#         x-=1
# for i in my_gen(8):
#     print(i)

x=int(input("enter the value of x : "))
def counter():
    i=1
    while(i<=x):
        yield i
        i+=1
for i in counter():
    print(i**2)