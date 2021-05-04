def magnets():
    magnets=int(input())

    magnets_stack=[]
    while magnets>0:
        magnets_stack.append(input())
        magnets-=1

    temp=magnets_stack[0]
    group=1
    for i in range(len(magnets_stack)-1):
        if temp==magnets_stack[i+1]:
            continue
        else:
            group+=1
            temp=magnets_stack[i+1]
    return group

print(magnets())