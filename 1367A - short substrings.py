n=int(input())
strings=list()
for i in range(n):
    strings.append(input())

# print(strings)

temp=''
for i in strings:
    for j in range(len(i)):
        if j%2==0:
            temp+=i[j]
    print(temp+i[-1])
    temp=''
    # print(i[::2]+i[-1])
    # print(x)
    # print(i[-1])
    # if len(set(i))==1:
    #     print(i[0]*((len(i)//2)+1))
    # else:
    #     temp+=i[0]
    #     # print(i[1: len(i) - 1])
    #     for j in range(1,len(i)-2):
    #         if i[j]==i[j+1]:
    #             temp+=i[j]
    #     temp+=i[len(i)-1]
    #     print(temp)
    #     temp=''




