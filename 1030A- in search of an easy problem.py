def easy_problem():
    people_voted=int(input())

    votes=input().split()

    if '1' in votes:
        return "HARD"
    else:
        return "EASY"

print(easy_problem())
