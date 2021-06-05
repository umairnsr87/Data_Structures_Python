def puzzles():
    n,m=map(int,input().split())
    puzzles=list(map(int,input().split()))
    puzzles.sort()


    minimum=1111111111

    for i in range(m - n + 1):
        t = puzzles[i:i + n ]
        minimum = min(minimum, t[-1] - t[0])
    return minimum


print(puzzles())
