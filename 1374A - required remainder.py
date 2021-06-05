x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    print(c-c%a+b) if c-c%a+b <= c else print(c-c%a-(a-b))
