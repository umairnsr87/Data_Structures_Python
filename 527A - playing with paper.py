a, b = map(int, input().split())
ans =0
while a > 0 and b > 0:
    if a >= b:
        ans = ans + a // b
        a = a % b
    else:
        ans = ans + b // a
        b = b % a

print(int(ans))