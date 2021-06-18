t = int(input())
for _ in range(t):
    permutation_len = int(input())
    permutation = list(map(int, input().split()))

    permutation_dict = {}

    for i in permutation:
        if i in permutation_dict:
            temp = permutation_dict[i]
            permutation_dict[i] = temp + 1
        else:
            permutation_dict[i] = 1
    x = list(permutation_dict.keys())
    for value in x[:permutation_len]:
        print(value, sep=' ')
