test = int(input())

for _ in range(test):
    n, x = map(int, input().split())
    ran = 1000
    ll, ul = 1, 2
    count = 1
    while ran > 0:
        # t = list(range(ll, ul + 1))
        if n in list(range(ll, ul + 1)):
            print(count)
            break
        else:
            ll = ul + 1
            ul = ul + x
            count += 1
            ran -= 1
