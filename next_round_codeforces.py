temp=input()
temp1=temp.split(" ")

n=int(temp1[0])
k=int(temp1[1])

p=input()
p=p.split(" ")
players=[]
for i in range(n):
    players.append(int(p[i]))

count=0
score=players[k-1]
# if k!=0:
for i in range(n):

    if players[i]>=score and (score!=0 or players[i]!=0):
        count+=1
    elif players[i]<score:
        break
print(count)
# a=[0,1,2,3,4,5,6]
# print(a[5])