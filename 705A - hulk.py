def hulk():
    n=int(input())

    list=[]
    for i in range(1,n+1):
        if i%2==0:
            list.append("I love that")
        else:
            list.append("I hate that")
    if list[len(list)-1]=="I love that":
        list[len(list) - 1]="I love it"
    else:
        list[len(list) - 1] = "I hate it"
    string=""
    for i in range(len(list)):
        string+=list[i]+" "
    return string
print(hulk())