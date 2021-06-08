shops=int(input())
prices_in_shops=list(map(int,input().split()))
prices_in_shops.sort()
days=int(input())

def search(array,length_of_array,element):
    initial_length=0
    final_length=length_of_array-1
    flag=0
    while initial_length <= final_length:
        center=(initial_length+final_length)//2
        if array[center]<=element:
            flag=center+1
            initial_length=center+1
        else:
            final_length=center-1
    return flag



for i in range(days):
    count = 0
    coins=int(input())
    # Solution 2: With time complexity of logN
    print(search(prices_in_shops,length_of_array=len(prices_in_shops),element=coins))


    # # Solution:1 with high time complexity
    # if coins>=prices_in_shops[len(prices_in_shops)//2]:
    #     for price_in_shop in prices_in_shops[len(prices_in_shops)//2:]:
    #         # prices_in_shops.index(price_in_shop)
    #         if coins >= price_in_shop:
    #             count += 1
    #         else:
    #             break
    #     print(len(prices_in_shops)//2+count)
    # else:
    #     for price_in_shop in prices_in_shops[:len(prices_in_shops)//2]:
    #         # prices_in_shops.index(price_in_shop)
    #         if coins >= price_in_shop:
    #             count += 1
    #         else:
    #             break
    #     print(count)
    # #

    # Soltion 0 with O(n)
    # for price_in_shop in prices_in_shops:
    #     # prices_in_shops.index(price_in_shop)
    #     if coins >=price_in_shop:
    #         count+=1
    #     else:
    #         break
    # print(count)