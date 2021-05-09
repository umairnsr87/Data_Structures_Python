x=int(input())

counter=0

while x!=0:
    if x-5>=0:
        counter+=1
        x-=5
    elif x-4>=0:
        counter+=1
        x-=4
    elif x-3>=0:
        counter+=1
        x-=3
    elif x-2>=0:
        counter+=1
        x-=2
    elif x-1>=0:
        counter+=1
        x-=1
print(counter)

