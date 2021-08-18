from collections import Counter

test = int(input())

strings = input()

# time complexity:O(n)
# while '01' or '10' in strings:
#     if '01' in strings:
#         strings = strings.replace('01', '')
#     elif '10' in strings:
#         strings = strings.replace('10', '')
#     else:
#         break
#
# print(len(strings))

# time complexity:O(1)
x = Counter(strings)
if (x['0'] == x['1']) and (x['0'] + x['1']) == len(strings):
    print(0)
elif not x['1'] or not x['0']:
    print(len(strings))
else:
    a = min(x['0'], x['1'])
    print(len(strings) - 2 * a)
