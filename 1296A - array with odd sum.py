test = int(input())

for _ in range(test):
    n = int(input())
    numbers = list(map(int,input().split()))
    odd=0
    even=0
    for num in numbers:
        if num%2!=0:
            odd+=1
        else:
            even+=1

    if ((odd==n and n%2==0) or even==n):
        print("NO")
    else:
        print("YES")
