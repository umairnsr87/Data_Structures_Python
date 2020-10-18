x=input()
y=input()

temp=''

for i in range(len(x)):
    if x[i]==y[i]:
        temp+='0'
    else:
        temp+='1'

print(temp)
