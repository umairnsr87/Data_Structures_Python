x=int(input())

numbers=input()
numbers=numbers.split(" ")

temp=0
low=int(numbers[0])
high=int(numbers[0])

for i in range(1,x):
    if int(numbers[i])>high:
        high=int(numbers[i])
        temp+=1
    elif int(numbers[i])<low:
        low=int(numbers[i])
        temp+=1

print(temp)