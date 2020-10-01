string=input()
vowel=['A','E','I','O','U','Y','y','a','e','i','o','u']
without_vow=[]
for i in range(len(string)):
    if string[i] in vowel:
        pass
    else:
        without_vow.append(string[i])
temp=''
for vow in without_vow:
    flag=vow.lower()
    temp+='.'+flag
print(temp)