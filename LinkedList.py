class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None
    def listtraverse(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

#creating the object of linkedlist and setting it to First created Node
list1=Linkedlist()
list1.headval=Node("Mon")

#cerating 2 extra nodes
e2=Node("Tue")
e3=Node("Wed")

#linked 1st node to 2nd node
list1.headval.nextval=e2
#link 2nd node to third
e2.nextval=e3

#traversion the linked list
list1.listtraverse()