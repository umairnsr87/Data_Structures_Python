def total_stages():
    levels=int(input())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    p=p[1:]
    q=q[1:]
    if len(set(p+q))==levels:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
total_stages()