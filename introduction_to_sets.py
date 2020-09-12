def average(array):
    # your code goes here
    temp=set(array)
    res=0
    for x in temp:
        res+=x
    return res/len(temp)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)