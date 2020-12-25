num_flowers=int(input())

flowers=[]

for i in range(num_flowers):
    flowers.append(int(input()))


maximum=flowers[0]
minimum=flowers[0]
counter1=0
counter2=0

for i in range(len(flowers)):
    if flowers[i]>maximum:
        maximum=flowers[i]

    if flowers[i]<minimum:
        minimum=flowers[i]

for i in range(len(flowers)):
    if flowers[i]==maximum:
        counter1+=1
    if flowers[i]==minimum:
        counter2+=1

print(str(maximum-minimum)+" "+str(counter1*counter2))