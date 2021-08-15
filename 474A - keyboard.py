a="qwertyuiopasdfghjkl;zxcvbnm,./"
orient=input()
pressed=input()
orig=""
for i in range(len(pressed)):
    if orient=="R":
        orig += a[a.find(pressed[i])-1]
    elif orient=="L":
        orig += a[a.find(pressed[i])+1]

print(orig)