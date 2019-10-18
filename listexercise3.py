l1=[1,2,3,4]
l2=[5,1,7,8]
def check_lists(l1,l2):
    # res = False
    for i in l1:
        for j in l2:
            if i==j:
                print('common')
            else:
                print('not')
print(check_lists(l1,l2))
