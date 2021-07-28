num = int(input())
scores = {}
for _ in range(num):
    score = input()
    if score in scores:
        temp = scores[score]
        scores[score] = temp + 1
    else:
        scores[score] = 1

val = 0
key = ''
for keys, values in scores.items():
    if val < values:
        val = values
        key = keys

print(key)
