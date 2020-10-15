# import re
x=int(input())
# temp=0

# for i in range(len(x)):
#     if x[i]=='4' or x[i]=='7':
#         temp+=1
# if temp==4 or temp==7:
#     print("YES")
# else:
#     print("No")

# text=re.sub(r'7','-',x)
# text=re.sub(r'4','-',text)
#
# temp='-'*len(x)
# if text==temp:
#     print("YES")
# else:
#     print("NO")
# dict={}
#
# for i in range(len(x)):
#     if x[i] in dict:
#         temp=dict[x[i]]
#         dict[x[i]]=temp+1
#     else:
#         dict[x[i]]=1
# # print(list(dict.keys()))
# # print(dict)
# if dict[7]:
#     print("YES")
# else:
#     print("NO")
temp=0
while(x):
    if x%10==7 or x%10==4:
        temp+=1
    x=x//10
if temp==7 or temp==4:
    print("YES")
else:
    print("NO")