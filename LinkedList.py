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

    def insertatfront(self,newdata):
        newnode=Node(newdata)
        newnode.nextval=self.headval
        self.headval=newnode
        print("Element Inserted")

    def insertatend(self,newdata):
        newnode=Node(newdata)
        if self.headval is None:
            self.headval=newnode
            return
        laste=self.headval
        while(laste.nextval):
            laste=laste.nextval
        laste.nextval=newnode

    def insertinbetween(self,middle_node,newdata):
        if middle_node is None:
            print("No such Node present")
            return
        newnode=Node(newdata)
        newnode.nextval=middle_node.nextval
        middle_node.nextval=newnode


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

#---------------------------------------------------
print("Traversed linked list is")
#traversion the linked list
list1.listtraverse()


#---------------------------------------------------
print("Insertion at front")
list1.insertatfront("Sun")
#traversion the linked list
list1.listtraverse()

#---------------------------------------------------
print("Insertion at the end")
list1.insertatend("sat")
#traversion the linked list
list1.listtraverse()

#---------------------------------------------------

list1.insertinbetween(list1.headval.nextval,"Fri")
print("The inbetween insertion leads to the list of")
#traversion the linked list
list1.listtraverse()
