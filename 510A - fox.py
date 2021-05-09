def fox(rows,columns):
    counter=0
    for i in range(1,rows+1):
        counter += 1
        if i%2!=0:
            print("#"*columns)
        elif i%2==0 and (counter/2)%2!=0:
            print("."*(columns-1)+"#")
        elif i % 2 == 0 and (counter / 2) % 2 == 0:
            print("#" +"."* (columns-1))

rows,columns=map(int,input().split())
fox(rows,columns)