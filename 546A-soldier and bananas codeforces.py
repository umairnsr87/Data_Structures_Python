x=input().split(" ")
# print(x)
flag=0
for i in range(1,int(x[2])+1):
    flag+=int(x[0])*i


if flag>int(x[1]):
    print(flag-int(x[1]))
else:
    print(0)