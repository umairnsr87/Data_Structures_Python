n,m,a,b=map(int,input().split())

total_cost_tkt=a*n

min_fare=total_cost_tkt
# pass_needed=

amount_pass=(n//m)*b

# Cost of 1 ticket is less
if float(a)<(b/m):
    print(a*n)
elif amount_pass+b>(amount_pass+(a*(n-(n//m)*m))):
    print((amount_pass+(a*(n-(n//m)*m))))
else:
    print(amount_pass+b)


# if amount_pass+b>=total_cost_tkt:
#     print(min_fare)
# else:
#     min_fare=amount_pass+a
#     print(min_fare)

# if (amount_pass+

# print(pass_needed,total_cost_tkt)