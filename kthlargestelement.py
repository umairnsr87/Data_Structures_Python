from collections import Counter
def kthlargest(array,number):
    #step1: sort the array first in the increasing order
    sort_dict={}
    for ele in array:
        ele=str(ele)
        if ele in sort_dict:
            sort_dict[ele]=sort_dict[ele]+1
            # print("The element is {}" .format(sort_dict[ele]))
        else:
            sort_dict[ele]=1
    unique_list=list(sort_dict.keys())
    unique_list.sort(reverse=True)
    print(unique_list)
    return unique_list[number-1]
    # elemens_dictinct=Counter(array).keys()
    # elemens_dictinct.sort(reverse=False)
    #it will give the sorted array
    # print("This is the kth largets number {}".format(elemens_dictinct[number-1]))

z=[1,2,3,3,3,4,5,6,7,7,8,9]
print(kthlargest(z,4))
# ex:[1,2,3,3,3,4,5,6,7,7,8,9]
# [9,8,7,6,5,4,3,2,1]

