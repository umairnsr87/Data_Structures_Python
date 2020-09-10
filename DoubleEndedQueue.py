from collections import deque

dou_end_queue=deque(["Mon","Tue","Wed","Thurs","Fri","Sat"])
print(dou_end_queue)

dou_end_queue.appendleft("Sun")
print(dou_end_queue)


dou_end_queue.append("Sun")
print(dou_end_queue)

dou_end_queue.pop()
print(dou_end_queue)


dou_end_queue.popleft()
print(dou_end_queue)
