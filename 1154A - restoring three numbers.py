def restoring_numbers():
    array=list(map(int,input().split()))
    array.sort()
    maxim=max(array)
    ac=array[0]
    ab=array[1]
    bc=array[2]
    b=maxim-ac
    c=maxim-ab
    a=maxim-bc
    return a,b,c

x=restoring_numbers()
print(x[0],x[1],x[2])



