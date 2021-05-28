n=int(input())
welfare=tuple(map(int,input().split()))

maximum=max(welfare)

total_welfare_to_be_distributed=0

if len(welfare)==1:
    pass
else:
    for i in range(len(welfare)):
        total_welfare_to_be_distributed+=maximum-welfare[i]
print(total_welfare_to_be_distributed)

