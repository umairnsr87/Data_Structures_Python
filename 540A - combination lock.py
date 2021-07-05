pattern_len = int(input())

pattern = list(input())
pattern_orig = list(input())

sum = 0
for i in range(len(pattern)):
    sum=sum+ min(abs(int(pattern[i])-int(pattern_orig[i])),(10-abs(int(pattern[i])-int(pattern_orig[i]))))

print(sum)