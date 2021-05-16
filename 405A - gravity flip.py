def gravity_flip():
    n=int(input())

    blocks=list(map(int,input().split()))
    blocks.sort(reverse=False)
    for i in blocks:
        print(i)


gravity_flip()