#step1: get the input
n, m = map(int,input().split())

#step2 :get all the letters in language 1 and 2
language1 = []
language2 = []
for _ in range(m):
    flag = input().split()
    language1.append(flag[0])
    language2.append(flag[1])
sentence = input().split()
for flag,string in enumerate(sentence):
    if string in language1:
        location=language1.index(string)
        if len(language1[location])> len(language2[location]):
            sentence[flag]=language2[location]

for word in sentence:
    print(word,sep=" ")
