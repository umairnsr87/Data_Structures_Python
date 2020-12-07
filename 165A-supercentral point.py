points=int(input())

points_tup=[]
for i in range(points):
    temp=tuple(input().split(" "))
    points_tup.append(temp)


count=0

# for tup in points_tup:
#     right = 0
#     left = 0
#     lower = 0
#     upper = 0
#     x=int(tup[0])
#     y=int(tup[1])
#     print(x,y)
#
#     for tup1 in points_tup:
#
#         x_ = int( tup1[0] )
#         y_ = int( tup1[1] )
#         print( x_, y_ )
#         if x==x_ and y==y_:
#             continue
#         else:
#             if x==x_ and y<y_:
#                 upper+=1
#             if x==x_ and y<y_:
#                 lower+=1
#             if y==y_ and x<x_:
#                 right+=1
#             if y==y_ and x>x_:
#                 left+=1
#             print(upper,lower,left,right)
#     if upper>1 and lower>1 and right>1 and left>1:
#         count+=1
#
# print(count)

for i in range(0,len(points_tup)):
    l=r=u=d=0;
    x=int(points_tup[i][0])
    y=int(points_tup[i][1])
    for j in range(0,len(points_tup)):
        if(int(points_tup[j][0])==x):
            if int(points_tup[j][1])>y:
                u+=1;
            elif int(points_tup[j][1])<y:
                d+=1

        elif(int(points_tup[j][1])==y):
            if(int(points_tup[j][0])>x):
                r+=1
            elif(int(points_tup[j][0])<x):
                l+=1;


    if(l>0 and r>0 and d>0 and u>0):
        count+=1;

print(count)