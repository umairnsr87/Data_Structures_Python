#
# def re_pattern_matching(pattern,data):
#     import re
#     raw_string=r''
#     for i in range(len(pattern)):
#         raw_string = raw_string + '.*' + pattern[i]
#     raw_string += '.*'
#
#     if  re.match(raw_string,data):
#         return True
#     else:
#         return False
def amusing_joke():
    guest_name = input()
    host_name = input()
    found_letters = input()
    # # host_re_pat=r''
    # # guest_re_pat=r''
    # # for i in range(len(guest_name)):
    # #     guest_re_pat=guest_re_pat+'.*'+guest_name[i]
    # # guest_re_pat+='.*'
    # #
    # # for i in range(len(host_name)):
    # #     host_re_pat=host_re_pat+'.*'+host_name[i]
    # # host_re_pat+='.*'
    #
    #
    # # guest_re_pat=re.match(re.match(r'.*h.*e.*l.*l.*o.*',message):)
    # # result=re.match(found_letters)
    # # print(guest_re_pat)
    # # print(host_re_pat)
    # # print(re_pattern_matching(host_name,found_letters))
    # # print(re_pattern_matching(guest_name,found_letters))
    #
    # # print(re.match(guest_re_pat,found_letters))
    # # if (len(guest_name)+len(host_name))<len(found_letters):
    # #     print("NO")
    # # elif  and :
    # #     print("YES")
    # # else:
    # #     print("idk")

    return "YES" if sorted(host_name + guest_name) == sorted(found_letters) else "NO"

print(amusing_joke())
