def pangram():
    import string
    length=int(input())
    input_string=set(input().lower())

    if length<26:
        return "NO"
    elif len(input_string)==len(string.ascii_lowercase):
        return "YES"
    else:
        return "NO"

print(pangram())
