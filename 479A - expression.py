a=int(input())
b=int(input())
c=int(input())



result=a*b*c

if a*(b+c)>result:
    # print("1")
    result=a*(b+c)
    # print(result)
if (a+b)*c>result:
    # print("11")
    result=(a+b)*c
    # print(result)
if a+b+c>result:
    # print("111")
    result=a+b+c
    # print(result)


print(result)


