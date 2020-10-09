import re
message=input()

if re.match(r'.*h.*e.*l.*l.*o.*',message):
    print("YES")
else:
    print("NO")

# dict={}
# string=['h','e','l','l','o']
# for i in range(len(message)):
#     if message[i]==string[0]:
#         print(message[i])
#         if message[i] == string[0]:
#             print( message[i] )

#     if message[i] in string:
#        if message[i] in dict:
#            temp=dict[message[i]]
#            dict[message[i]]=temp+1
#        else:
#            dict[message[i]] = 1
#
# if dict["h"]>=1 and dict["e"]>=1 and dict["l"]>=2 and dict["o"]>=1:
#     print("YES")
# else:
#     print("NO")
# print(dict["h"]>=1)
        # print(message[i])
# temp=set(temp)
# temp2=set(string)

# if temp==temp2:
#     print(True)
# else:
#     print(False)