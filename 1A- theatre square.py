def square():
    import math
    n,m,a=map(int, input().split())
    return math.ceil(n/a)*math.ceil(m/a)

print(square())