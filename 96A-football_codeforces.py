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


if a>=7 or b>=7:
    print("YES")
else:
    print("NO")