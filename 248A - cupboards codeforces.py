x=int(input())

list=[]
for i in range(x):
    temp=input()
    list.append(temp)
    # temp.split(" ")

leftopen=0
leftclose=0
rightopen=0
rightclose=0
#step2: iterate through every door
for i in range(len(list)):
    x=list[i].split(" ")
    #left close
    if x[0]=="0":
        leftclose+=1
    #left open
    if x[0]=="1":
        leftopen+=1
    #right open
    if x[1]=="1":
        rightopen+=1

    #right close
    if x[1]=='0':
        rightclose+=1

# print(leftopen,leftclose,rightopen,rightclose)
temp=0
if leftopen>leftclose:
    temp+=leftclose
    if rightopen>rightclose:
        temp+=rightclose
    else:
        temp+=rightopen
else:
    temp+=leftopen
    if rightopen>rightclose:
        temp+=rightclose
    else:
        temp+=rightopen

print(temp)
