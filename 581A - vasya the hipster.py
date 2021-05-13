def socks_pairs():
    a,b=map(int,input().split())

    print(min(a,b),(((a+b)-(min(a,b)*2)))//2)
socks_pairs()