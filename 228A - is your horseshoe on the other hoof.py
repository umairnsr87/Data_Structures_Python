def different_horseshoe():
    x = tuple(map(int, input().split()))
    total_horseshoe = len(x)
    set_total_horseshoe = set(x)
    return total_horseshoe - len(set_total_horseshoe)


print(different_horseshoe())