import string
import random

chars = string.ascii_lowercase

test = int(input())
for _ in range(test):
    n, a, b = map(int, input().split())
    temp = ""
    initial = chars[:b]
    while len(temp) < n:
        diff = n - len(temp)
        if diff > b:
            temp += initial
        else:
            temp += initial[:diff]
    print(temp)
