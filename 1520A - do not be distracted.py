test=int(input())
for i in range(test):
    num=int(input())
    tasks=list(input())
    val_dict=[]
    diff_count=0
    
    while diff_count<num:
        if (len(val_dict)==0):
            val_dict.append(tasks[diff_count])
        elif val_dict[-1]!=tasks[diff_count]:
            val_dict.append(tasks[diff_count])
        diff_count+=1
        
    if sorted (val_dict)==sorted(set(tasks)):
        print("YES")
    else:
        print("NO")
