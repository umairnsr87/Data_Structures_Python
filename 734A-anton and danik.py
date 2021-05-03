def winner():
    games_played= int(input())
    results = input()
    a = 0
    d = 0

    for i in range(games_played):
        if results[i]=='A':
            a +=1
        elif results[i] == 'D':
            d +=1

    if a==d:
        return "Friendship"
    elif a>d:
        return "Anton"
    else:
        return "Danik"

print(winner())