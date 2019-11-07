N = int(input("enter the number of students : "))
students = list()
for i in range(N):
    name=input("enter the name of the students : ")
    score=float(input("enter the score of the student : "))
    students.append([name, score])
# for i in range(N):
#     students.append([name,score])
#     # students.append([input(), float(input())])
# print(students)

scores = set([students[x][1] for x in range(N)])
scores = list(scores)
scores.sort()

students = [x[0] for x in students if x[1] == scores[1]]
students.sort()

for s in students:
    print(s)