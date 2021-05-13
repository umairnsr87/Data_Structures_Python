def police_recruits():
    n=int(input())
    recruits=list(map(int,input().split()))

    crime_count=0
    police_count=0

    for i in range(len(recruits)):
        if recruits[i]==-1 and police_count==0:
            crime_count+=1
        elif recruits[i]==-1 and police_count>0:
            police_count-=1
        elif recruits[i]>=1:
            police_count+=recruits[i]

    return crime_count

print(police_recruits())