list1=['abc','xyz','aba','1221']

def count_strings():
    count = 0
    for i in list1:
        if len(i)>2 and i[0] == i[-1]:
            count += 1
    return count

print(count_strings())
