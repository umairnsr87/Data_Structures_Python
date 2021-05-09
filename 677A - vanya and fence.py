def fence_height():
    n,h=map(int,input().split())

    friends_height=list(map(int,input().split()))

    width_of_road=0

    for i in range(len(friends_height)):
        if friends_height[i]<=h:
            width_of_road+=1
        elif friends_height[i]>h:
            width_of_road+=2

    return width_of_road
print(fence_height())