def new_year_candles():
    a,b = map(int,input().split())
    count = a
    while a!= 0:
        count += (a//b)
        a = (a % b)+(a//b)

        if a < b:
            break
    return count


print(new_year_candles())