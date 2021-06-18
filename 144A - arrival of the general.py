n=int(input())
lst=list(map(int,input().split()))

mx = lst.index(max(lst))
mi = lst[::-1].index(min(lst))  #index of minimum from end
if mx < (len(lst) - 1 - mi):
    print(mi + mx)
else:
    print(mx+mi-1)

# count=0
# for j in range(len(soldiers)):
#     if soldiers[0] == max(soldiers) and soldiers[len(soldiers) - 1] == min(soldiers):
#         print(count)
#         break
#     for i in range(len(soldiers)-1):
#         count+=1
#         if soldiers[i]<soldiers[i+1]:
#             temp=soldiers[i+1]
#             soldiers[i+1]=soldiers[i]
#             soldiers[i]=temp
#
#             if soldiers[0] == max(soldiers) and soldiers[len(soldiers) - 1] == min(soldiers):
#                 print(count)
#                 break



#
# passes=0
# counter=0
# # while True:
# #     if soldiers[0]==max(soldiers) and soldiers[len(soldiers)-1]==min(soldiers):
#
# for i in range(n-1):
#     for j in range(n,n-i-1):
#         if soldiers[j] > soldiers[j + 1]:
#             soldiers[j], soldiers[j + 1] = soldiers[j + 1], soldiers[j]
#             passes += 1
#         # if soldiers[0] == max(soldiers) and soldiers[len(soldiers) - 1] == min(soldiers):
#         #     print(passes)
#         #     break
#
#
# print(soldiers)
# print()
#
#
#
#


# Python program for implementation of Bubble Sort

# def bubbleSort(arr):
#     passes=0
#     n = len(arr)
#     # Traverse through all array elements
#     for i in range(n-1):
#     # range(n) also work but outer loop will repeat one time more than needed.
#
#         # Last i elements are already in place
#         for j in range(0, n-1):
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
#         if arr[0] == max(arr) and soldiers[len(arr) - 1] == min(arr):
#             print(passes)
#             return i        # break
#
#     return passes
# Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]

# print(bubbleSort(soldiers))

# print ("Sorted array is:")
# for i in range(len(soldiers)):
# 	print ("%d" %soldiers[i]),
