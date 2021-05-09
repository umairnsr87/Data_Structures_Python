def magnets():
    magnets=int(input())

    magnets_stack=[]
    for x in range(magnets):
        magnets_stack.append(input())

    temp=magnets_stack[0]
    group=1
    for i in range(len(magnets_stack)-1):
        if temp!=magnets_stack[i+1]:
            group += 1
            temp = magnets_stack[i + 1]
    return group

print(magnets())