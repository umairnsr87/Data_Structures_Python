#step1:create a queue class
class Queue:
    def __init__(self):
        self.queue=list()
    def enqueue(self,value):
        if value not in self.queue:
            self.queue.insert(0,value)
            print("Inserted element {} in queue".format(value))
            return True
        return False
    def dequeue(self):
        if len(self.queue)>0:
            self.queue.pop()
            print("Element deleted from queue and queue after deletion of element is {}".format(self.queue))
            return True
        else:
            print("No element in Queue")
            return False



queue=Queue()

#inserty element into queue
queue.enqueue("Mon")
queue.enqueue("Trues")
queue.enqueue("wed")
#removing element from the queue
queue.dequeue()