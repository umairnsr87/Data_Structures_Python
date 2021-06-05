def this_coach_is_worst():
    test_cases=int(input())
    for i in range(test_cases):
        members_in_team=int(input())
        members=list(map(int,input().split()))
        members.sort()
        minimum=max(members)
        for i in range(len(members)-1):
            if (abs(members[i]-members[i+1]))<minimum:
                minimum=abs(members[i]-members[i+1])
        print(minimum)
    
this_coach_is_worst()