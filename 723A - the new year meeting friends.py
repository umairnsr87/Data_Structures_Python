def meeting_friends():
    a=list(map(int,input().split()))
    a.sort()

    distance=0

    splitter=len(a)//2

    for i in range(len(a)):
        if a[i]==a[splitter]:
            continue
        else:
            distance+=abs(a[i]-a[splitter])
    return distance

print(meeting_friends())
