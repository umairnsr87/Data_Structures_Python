import re
song=input()

updated=re.sub("WUB"," ",song)
# while(updated[0]==" "):
#     pattern=re.compile(r"\S")
#     updated=re.sub(pattern,"",updated)

updated=updated.strip()
print(updated)