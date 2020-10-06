y=input()
x=y.split("+")

temp=""
x.sort()
for p in x:
    temp+=p+"+"

print(temp[:len(y)])