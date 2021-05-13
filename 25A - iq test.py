def iq_test():
    n=int(input())
    num=list(map(int,input().split()))

    odd_list=[]
    even_list=[]
    for i in range(len(num)):
        if num[i]%2==0:
            even_list.append(num[i])
        else:
            odd_list.append(num[i])

    if len(odd_list)>len(even_list):
        return num.index(even_list[0])+1
    else:
        return num.index(odd_list[0])+1

print(iq_test())