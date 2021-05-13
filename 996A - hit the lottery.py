def lottery():
    amount=int(input())
    count=0
    #sol:1(high time complexity
    # while amount!=0:
    #     if amount>=100:
    #         amount-=100
    #         count+=1
    #     elif amount>=20:
    #         amount-=20
    #         count+=1
    #     elif amount>=10:
    #         amount-=10
    #         count+=1
    #     elif amount>=5:
    #         amount-=5
    #         count+=1
    #     elif amount>=1:
    #         amount-=1
    #         count+=1
    # print(count)

    #sol:2:for time complexity
    while amount>0:
        if amount>=100:
            count += amount // 100
            amount = amount % 100

        elif amount>=20:
            count += amount // 20
            amount = amount % 20
        elif amount>=10:
            count += amount // 10
            amount = amount % 10
        elif amount>=5:

            count += amount // 5
            amount = amount % 5
        elif amount>=1:
            count += amount // 1
            amount = amount % 1
    return count

print(lottery())