n=int(input())
students=list(map(int,input().split()))

t1index=[]
t2index=[]
t3index=[]
for i in range(len(students)):
    if students[i]==1:

        t1index.append(i+1)
        # t1index.append(students.index(students1[i]))
        # students.pop(students.index(students1[i]))

    elif students[i]==2:
        t2index.append(i+1)
        # t2index.append(students.index(students1[i]))
        # students.pop(students.index(students1[i]))
    elif students[i]==3:
        # t3index.append(students.index(students1[i]))
        t3index.append(i+1)
        # students.pop(students.index(students1[i]))
# #
# print(t1,t1index)
# print(t2,t2index)
# print(t3,t3index)

minimum=min(len(t2index),len(t1index),len(t3index))
if len(t2index)==0 or len(t1index)==0 or len(t3index)==0:
    print(0)
else:
    print(minimum)
    for i in range(minimum):
        print(f'{t1index[i]} {t2index[i]} {t3index[i]}')