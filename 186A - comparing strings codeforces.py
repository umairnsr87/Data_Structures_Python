gene1=input()
gene2=input()

n=min(len(gene1),len(gene2))
z=0
if sorted(gene1)==sorted(gene2):
    for t in range(n):
        if gene1[t]!=gene2[t]:
            z+=1
    if z==2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


