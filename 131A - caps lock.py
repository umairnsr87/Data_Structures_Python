def capsLock():
    s = input().strip()
    if s.isupper():
        return s.lower()
    elif s[0].islower() and (not s[1:] or s[1:].isupper()):
        return s.capitalize()
    else:
        return s


print(capsLock())

# letter=input()
#
# list=list(letter)
# upper=0
# lower=0
# for l in list:
#     if l.isupper():
#         upper+=1
#     else:
#         lower+=1
#
# if (list[0].islower() and lower<=1 ) or (upper==len(list) and lower==0):
#     list[0] = list[0].upper()
#     for i in range(1, len(list)):
#         list[i] = list[i].lower()
#     print(''.join(list))
# else:
#     print(''.join(list))
#
#
#
# # upper=0
# # lower=0
# # for i in list:
# #     if i.islower():
# #         lower+=1
# #     else:
# #         upper+=1
# #
# # # print(f'{lower} is lower and {upper} is upper')
# #
# # if lower>1:
# #     print(''.join(list))
# # elif lower<1 and lower!=1:
# #     list[0] = list[0].upper()
# #     for i in range(1, len(list)):
# #         list[i] = list[i].lower()
# #     print(''.join(list))
# # elif lower==1:
# #     list[0]=list[0].upper()
# #     for i in range(1,len(list)):
# #         list[i]=list[i].lower()
# #     print(''.join(list))
#
#
#
#
#
# # lower=0
# #
# # for i in range(len(letter)):
# #     list.append(letter[i])
# #     if list[i].islower():
# #        lower+=1
# #
# #
# # if lower>1:
# #     print(''.join(list))
# # elif lower < 1:
# #     list[0] = list[0].upper()
# #     for i in range(1, len(list)):
# #         list[i] = list[i].lower()
# #     print(''.join(list))
# # elif lower==1 and list[0].islower():
# #     list[0]=list[0].upper()
# #     for i in range(1,len(list)):
# #         list[i]=list[i].lower()
# #     print(''.join(list))
#
#
# # if list[0].islower():
# #     list[0]=list[0].upper()
# #
# # for i in range(1,len(list)):
# #     list[i]=list[i].lower()
# #
# # joint=''.join(list)
#
#
# # print(joint)
#
#
# # print(list)
