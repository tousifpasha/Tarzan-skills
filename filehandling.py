# #to create a new file and to write a content in the file
#
# new_file = open('sample.txt', 'w')
# content ='this is python programming\npython programming is a easy way of writing a codes\nit is similar to c and c++'
# new_file.write(content)
# print(new_file)
# new_file.close()
#
#
# #To read a file contents
# new_file = open('sample.txt', 'r')
# print(new_file.read())
# new_file.close()


# To print a file contents as in the file

# new_file = open('sample.txt', 'r')
# print(new_file)
# for each in new_file :
#   print(each)


#to append meand to add data to the existing file
# new_file=open('sample.txt', 'a')
# new_file.write("This is an assembly level langauge")
# new_file.close()


#to create a file "with open" and write and it is not needed to close
# with open('sample1.txt', 'w') as f:
#     f.write('salman')

#to read a file without using close
# with open('sample1.txt', 'r') as f:
#     print(f.read())

#to take curson to some position and read and write the data
# with open('sample1.txt', 'w') as f:
#     f.write("salman ")
#     f.seek(9)
#     f.write('Ahmed')
#
# with open('sample1.txt', 'r') as f:
#     print(f.read())


#to copy contents from one file to another file
# with open('sample.txt', 'r') as rf:
#     with open('sample2.txt', 'w') as wf:
#         for i in rf:
#             print(wf.write(i))

#with open('sample2.txt,'r') as f:
#    print(f.read())


#to copy image from one file to another
# with open('tiger.jpeg', 'rb') as f:
#     with open('tigercopy.jpeg', 'wb') as wf:
#         for i in f:
#             wf.write(i)


#to read single line from the file

# with open('sample.txt', 'r+') as file:
#     data=file.readline()
#     print(data)


#to read the lines from the files

with open('sample.txt', 'r+') as file:
    data= file.readlines()
    print(data)


































