times=int(input())
inputs=[]
for i in range(times):
    temp=input()
    inputs.append(temp)

for val in inputs:
    if len(val)>10:
        print(val[0]+str(len(val)-2)+val[-1])
    else:
        print(val)
# print(inputs)