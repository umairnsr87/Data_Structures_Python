import  copy
x=int(input())
y = copy.deepcopy( x )


# dict={}

while(x<=9012):
    # print( x )
    val = []
    p = copy.deepcopy( x )

    while (p > 0):
        temp = p % 10
        val.append( temp )
        p = p // 10
    count = 0
    temp1 = 0
    for value in val:
        temp1=temp1+(10**count)*int(value)
        count+=1
# print(temp)
#     print(len(set(val)))
#     print("temp1 {}".format(temp1))
    if len(set(val))>=4 and temp1>y:
        print(temp1)
        break

    x+=1

# print(val)
