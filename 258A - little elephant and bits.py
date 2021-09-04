number = list(input())

if '0' in number:
    for i in range(len(number)):
        if number[i] == '0':
            number[i] = ''
            break
    number.pop(number.index(''))
    print(''.join(number))
else:
    print(''.join(number[1:]))
