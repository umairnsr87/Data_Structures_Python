test = int(input())

for _ in range(test):
    length = int(input())
    sequence = list(map(int, input().split()))
    fav_seq = []
    for seq in range(1, length+1):
        if seq % 2 != 0:
            fav_seq.append(sequence[0])
            sequence.pop(0)
        else:
            fav_seq.append(sequence[-1])
            sequence.pop()

    print(*fav_seq)
