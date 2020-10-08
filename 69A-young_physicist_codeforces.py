
times=int(input())

a,b,c=0,0,0
for i in range(times):
    x=input().split()
    # input_list.append(x)

    for p in range(len(x)):
        a += int(x[0])
        b += int(x[1])
        c += int( x[2] )

counter=a+b+c
# print(a,b,c)
# for i in range(len(input_list[0])):
#     input_list[i][i]+input_list[i+1][i]+input_list[i+2][i]
# print(input_list)
if a==0 and b==0 and c==0:
    print("YES")
else:
    print("NO")