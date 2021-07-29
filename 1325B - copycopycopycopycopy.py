test = int(input())

for _ in range(test):
    length_of_sequence = int(input())
    sequence = list(map(int, input().split()))
    print(len(set(sequence)))