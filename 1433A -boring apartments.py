t=int(input())
for m in range(t):

    x=input()

    value=int(x[0])
    s=[]
    for i in range(1,value+1):
        if i*1!=int(x):
            s.append(i*1)
        else:
            break
        if i * 11 != int(x):
            s.append(i*11)
        else:
            break
        if i * 111 != int(x):
            s.append(i*111)
        else:
            break
        if i * 1111 != int(x):
            s.append(i*1111)
        else:
            break

    pressed_keys=0
    for i in s:
        pressed_keys+=len(str(i))
    print(pressed_keys+len(x))

