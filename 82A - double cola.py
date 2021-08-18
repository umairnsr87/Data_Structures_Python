names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
n = int(input())
r = 1
if n<=5:
    print(names[n-1])
else:
    while r * 5 < n:
        n = n - (r*5)
        r = r * 2
    k = n//r


    print(names[k])