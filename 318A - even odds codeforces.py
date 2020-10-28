x=input()
x=x.split(" ")
# even=[]
# odds=[]
# for i in range(1,int(x[0])+1):
#     if i%2==0:
#         even.append(i)
#     else:
#         odds.append(i)
# temp=tuple(odds+even)
# print(temp[int(x[1])-1])


#step1:find the total number of odds and evens
odd=0
even=0
if int(x[0])%2==0:
    odd=int(x[0])//2
    even=int(x[0])//2
else:
    odd = (int( x[0] ) // 2)+1
    even = int( x[0] ) // 2
#
# print(odd,even)
#step2: odd quantity is grater than the number printed
if odd>=int(x[1]):
    print(1+(int(x[1])-1)*2)
else:
    print(2+((int(x[1])-odd)-1)*2)