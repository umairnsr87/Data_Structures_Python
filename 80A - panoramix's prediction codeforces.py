x=input()

x=x.split(" ")
prime=[]
# for i in range():
for num in range( int( x[0] ), int( x[1] )+1 ):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range( 2, num ):
            if (num % i) == 0:
                break
        else:
            # print( num )
            prime.append(num)
for i, j in enumerate(prime):
    if j == int(x[0]):
        if len(prime)>=2:
            if prime[i+1]==int(x[1]):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
# print(prime)
