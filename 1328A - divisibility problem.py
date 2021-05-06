total_numbers=int(input())



#sol:1
# for i in range(total_numbers):
#     a,b=map(int,input().split())
    # x=0
    # while a%b!=0:
    #     x+=1
    #     a+=1
    # print(x)
    # x=0


# sol:2
for i in range(total_numbers):
    a,b=map(int,input().split())
    print((b - a % b) % b);


