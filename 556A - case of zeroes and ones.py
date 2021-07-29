test = int(input())

strings = input()

while '01' or '10' in strings:
    if '01' in strings:
        strings = strings.replace('01', '')
    elif '10' in strings:
        strings = strings.replace('10', '')
    else:
        break

print(len(strings))