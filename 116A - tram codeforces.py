x=int(input())
list=[]
total_passengers=0
max_cap=0

for i in range(x):
    temp=input()
    list.append(temp)
# print(list)
for i in range(len(list)):
    flag=list[i].split(" ")
    total_passengers=total_passengers+int(flag[1])-int(flag[0])
    if total_passengers> max_cap:
        max_cap=total_passengers

print(max_cap)

