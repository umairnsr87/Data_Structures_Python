def binarysearch(array,low,high,element):
    if high >= low:

        mid = (high+low) // 2

        if array[mid]==element:
            return mid
        elif array[mid]>element:
            return binarysearch(array,low,mid-1,element)
        else:
            return binarysearch(array,mid+1,high,element)
    else:
        return -1

list_elements=[10,1,5,7,50,52,45]

print(list_elements)
list_elements.sort()
print(list_elements)

element=binarysearch(list_elements,0,len(list_elements)-1,52)
if element==-1:
    print("No such element present")
else:
    print("element present at {} position in the array".format(element))
