list=['hat', 'cat', 'mat']

def lcf(string):
    if not string:
        return ''
    prefix=string[0]

    for w in string:
        if len(prefix)>len(w):
            prefix,w=w,prefix

        while(len(prefix)>0):
            if w[:len(prefix)]==prefix:
                break
            else:
                prefix=prefix[:-1]

    return prefix


    # prefix=''
    # for val in string:

    # if len(string)==1:
    #     return string[0]
    # if string==[]:
    #     return ''
    # string.sort()
    # prefix=''
    # shortest=string[0]
    # for i in range(len(string)):
    #     #if values are equal the add to prefix
    #     if string[len(string)-1][i]==shortest[i]:
    #         prefix+=string[len(string)-1][i]
    #     else:
    #         #if not then break rhe loop
    #         break
    #     return prefix
p=lcf(list)
print(p)