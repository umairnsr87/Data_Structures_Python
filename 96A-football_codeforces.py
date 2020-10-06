x=input()
a=0
b=0
for i in range(len(x)):
    if x[i]=="1":
        a+=1
        b=0
    elif x[i]=="0":
        b+=1
        a=0
    if a>=7 or b>=7:
        break


    # if i+1==len(x):
    # if x[i]==x[i-1]:
    #     counter+=1
    # else:
    #     counter=1
# print("NO")
#         elif i+1<len(x):
#             if x[i]==x[i+1]:
#                 counter+=1
if a>=7 or b>=7:
    print("YES")
else:
    print("NO")