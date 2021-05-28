def vasya_and_socks():
    n, m = map(int, input().split())

    count = 1

    while count <= n:
        if count % m == 0:
            n = n + 1
        count += 1

    return count - 1


print(vasya_and_socks())
