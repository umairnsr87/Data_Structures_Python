cards = int(input())

card_numbers = list(map(int, input().split()))

sc1 = 0
sc2 = 0
for i in range(cards):
    if i % 2 == 0:
        start = card_numbers[0]
        end = card_numbers[-1]

        if start >= end:
            sc1 += start
            card_numbers.pop(0)
        else:
            sc1 += end
            card_numbers.pop()
    else:
        start = card_numbers[0]
        end = card_numbers[-1]

        if start >= end:
            sc2 += start
            card_numbers.pop(0)
        else:
            sc2 += end
            card_numbers.pop()

print(sc1, sc2)
