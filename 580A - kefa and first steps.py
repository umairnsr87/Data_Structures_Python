#step1:input
length=int(input())

numbers=list(map(int,input().split()))

count=1
length_of_biggest_sequence=1

for i in range(len(numbers)-1):
    #step2:checking if the next number is greater than the first number
    if numbers[i+1]>=numbers[i]:
        #incrementing the counts of the sequence
        count+=1
    else:
        count=1
    #checking if the new sequence is bigger or not
    length_of_biggest_sequence=max(length_of_biggest_sequence,count)

print(length_of_biggest_sequence)