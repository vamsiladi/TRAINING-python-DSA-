class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
        
class slinkedlist:
    def __init__(self):
        self.headval=None
        
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
            
    def atbegin(self,newdata):
        newnode=node(newdata)
        newnode.nextval=self.headval
        self.headval=newnode

    def atend(self,newdata):
        newnode=node(newdata)
        if self.headval == None:
            self.headval=newnode
        else:
            n=self.headval
            while n.nextval is not None:
                n=n.nextval
            n.nextval=newnode

    def inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        newnode=node(newdata)
        newnode.nextval=middle_node.nextval
        middle_node.nextval=newnode

    def delete_at_start(self):
        if self.headval is None:
            print("The list ha no elements")
            return
        self.headval=self.headval.nextval

    def delete_at_end(self):
        if self.headval is None:
            print("The list has no elements")
            return
        n=self.headval
        while n.nextval.nextval is not None:
            n=n.nextval
        n.nextval=None

    def delete_element_by_value(self,x):
        if self.headval is None:
            print("The list has no element to delete")
            return
        if self.headval.item==x:
            self.headval=self.headval.nextval
            return
        n=self.headval
        while n.nextval is not None:
            if n.nextval.item==x:
                break
            n=n.nextval
        if n.nextval is None:
            print("item not found in the list")
        else:
            n.nextval=n.nextval.nextval

    def reverse(self):
        prev=None
        current=self.headval
        while(current is not None):
            next1=current.nextval
            current.nextval=prev
            prev=current
            current=next1
        self.headval=prev


list=slinkedlist()
list.atbegin(20)
list.atbegin(4)
list.atbegin(15)
list.atbegin(85)
print("given linked list")
list.listprint()
list.reverse()
print("\n reversed linked list")
list.listprint()



        
