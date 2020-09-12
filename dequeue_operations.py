# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == "__main__":
    d = deque()
    n = int( input() )
    for i in range( n ):
        s = input().split()
        for i in range( 1, len( s ) ):
            s[i] = int( s[i] )

        if s[0] == "append":
            d.append( s[1] )
        if s[0] == "appendleft":
            d.appendleft( s[1] )
        if s[0] == "pop":
            d.pop()
        if s[0] == "popleft":
            d.popleft()

    tempstr = ""
    for ele in d:
        tempstr += str( ele ) + " "
    print( tempstr )



