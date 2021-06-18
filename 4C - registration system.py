n=int(input())

users={}

for i in range(n):
    username=input()
    counter=1
    if username in users:

        temp=users[username]
        users[username]=temp+1
        print(username+str(users[username]))
    else:
        users[username]=0
        print("OK")


