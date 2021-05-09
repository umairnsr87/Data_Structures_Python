set = input()
set = set.replace('{', '')
set = set.replace('}', '')
set = set.replace(' ', '')

list = list(set.split(','))
if '' in list and len(list) == 1:
    print(0)
else:
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    print(len(dict))
