name=input()
list_alpha=[]
for i in range(len(name)):
    list_alpha.append(name[i])

set_unique=set(list_alpha)

if len(set_unique)%2!=0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
