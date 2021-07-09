table_card = list(input())
cards_in_hands = list(input().split())

play = False
for card in cards_in_hands:
    _ = list(card)
    if _[1] == table_card[1] or _[0] == table_card[0]:
        play = True
        break


print("YES") if play else print("NO")
