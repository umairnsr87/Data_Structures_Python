#step1:get the input
op_count=int(input())

#define the operation
increment=["X++","++X","x++","++x"]
decrement=["X--","--X","x--","--x"]
operation_list=[]

#step3:get the values of input operations
for i in range(op_count):
    operation_list.append(input())

#step4:create the operation counter
flag=0

#step5:perform the operations
for operation in operation_list:
    if operation in increment:
        flag+=1
    elif operation in decrement:
        flag-=1

print(flag)