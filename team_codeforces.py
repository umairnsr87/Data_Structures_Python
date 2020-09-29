flag=int(input())

answers=[]
counter=0
for i in range(flag):
    temp1=input()
    tempx=temp1.split(" ")
    # print(tempx[0],tempx[1],tempx[2])
    # temp2 = int( input() )
    # temp3 = int( input() )
    answers.append([int(tempx[0]),int(tempx[1]),int(tempx[2])])
# print(answers)

# i=0
for answer in answers:
    temp=0
    for x in range(3):
        # print(answer[x])
        if answer[x]==1:
            temp+=1
    if temp>=2:
        counter+=1


print(counter)