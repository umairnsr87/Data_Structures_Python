a=int(input())
b=int(input())
c=int(input())



result=a*b*c

if a*(b+c)>result:
    result=a*(b+c)

if (a+b)*c>result:
    result=(a+b)*c

if a+b+c>result:
    result=a+b+c


print(result)


