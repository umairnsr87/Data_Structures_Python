for _ in range(int(input())):
    num = int(input())
    brackets = input()

    while '()' in brackets:
        brackets = brackets.replace("()", "")
    print(len(brackets)//2)