employees = int(input())

ways=0
for i in range(1,employees):
    tl=i
    members=employees-tl
    if members%tl == 0:
        ways+=1
print(ways)
