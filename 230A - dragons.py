def dragons():
    initial_strength_kirito,number_of_dragons=map(int,input().split())

    dragons_killed=0
    a=[]
    for i in range(number_of_dragons):
        a.append(list(map(int,input().split())))
        """
        Sorting since kirito can fight dragon in any order so 
        if kirito will start figting with the least strength dragon then 
        there is a chance that kirito strength will get greater than the dragon's strength
        """

    a.sort()
    for i in a:
        if i[0]<initial_strength_kirito:
            initial_strength_kirito+=i[1]
            dragons_killed+=1
        else:
            break

    if dragons_killed==number_of_dragons:
        return "YES"
    else:
        return "NO"

print(dragons())