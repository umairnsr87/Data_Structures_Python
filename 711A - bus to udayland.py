test = int(input())
seating = []
for _ in range(test):
    seats = input()
    seating.append([seats])

can_sit_together = 'NO'
for i in range(len(seating)):
    seatings = seating[i][0].split('|')
    if 'OO' in seatings[0]:
        seating[i][0] = (seatings[0].replace('OO', '++') + '|' + seatings[1])
        can_sit_together = 'YES'
        break
    elif 'OO' in seatings[1]:
        seating[i][0] = (seatings[0] + '|' + seatings[1].replace('OO', '++'))
        can_sit_together = 'YES'
        break

if can_sit_together == "YES":
    print(can_sit_together)

    for i in range(len(seating)):
        print(seating[i][0])
else:
    print("NO")
