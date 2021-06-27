test= int(input())

for _ in range(test):
    w,h,n = map(int,input().split())
    
    initial_sheet=1
    while( w%2==0):
        w=w//2
        initial_sheet*=2
    while( h%2==0):
        h=h//2
        initial_sheet*=2
    
    val="YES" if initial_sheet>=n else "NO"
    print(val)
    
