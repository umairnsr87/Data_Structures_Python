

#sol:1
# num=0
# for i in range(1,n+1):
#     if i%2==0:
#         num+=i
#     else:
#         num-=i
# print(num)


#sol:2

def calculating_function():
    n = int(input())
    if n%2==0:
        return n//2
    else:
        return -(n+1)//2


print(calculating_function())

