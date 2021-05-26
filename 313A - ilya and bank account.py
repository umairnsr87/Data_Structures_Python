def ilya_bribed_bank_manager():
    x = list(input())

    y = x.copy()
    z = x.copy()

    length = len(x)
    y.pop(length-1)
    z.pop(length-2)

    if int(''.join(x)) > 0:
        return int(''.join(x))
    elif int(''.join(y)) > int(''.join(z)):
        return int(''.join(y))
    else:
        return int(''.join(z))


print(ilya_bribed_bank_manager())