_=int(input())
chris=0
mishka=0
for i in range(_):
    d1,d2=map(int,input().split())
    if d1>d2:
        mishka+=1
    elif d1<d2 :
        chris+=1

if chris>mishka:
    print("Chris")
elif chris<mishka:
    print("Mishka")
elif chris==mishka:
    print("Friendship is magic!^^")




