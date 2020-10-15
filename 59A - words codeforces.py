x=input()

# print(x.isupper())
upper=0
lower=0
for i in range(len(x)):
    if x[i].isupper():
        upper+=1
    else:
        lower+=1

if upper>lower:
    print(x.upper())
else:
    print(x.lower())
