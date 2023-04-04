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

    def search_item(self,x):
        if self.headval is None:
            print("List has no elements")
            return
        n=self.headval
        while n is not None:
            if n.item == x:
                print("item found")
                return True
            n=n.nextval
        print("item not found")
        return False

    def get_count(self):
        if self.headval is None:
            return 0
        n=self.headval
        count=0
        while n is not None:
            count=count+1
        print(count)



    def insert_at_index(self,index,data):
        if index==1:
            newnode = node(data)
            newnode.nextval=self.headval
            self.headval=newnode
        i=1
        n=self.headval
        while i<index-1 and n is not None:
            n=n.nextval
            i=i+1
        if n is None:
            print("Index ")
        
            
            
        
list=slinkedlist()
list1=slinkedlist()
list2=slinkedlist()

list1.headval=node("mon")

e3=node("Wed")
list.headval.nextval=e2=node("Tue")
e2.nextval=e3
list.atbegin("sun")

list.inbetween(list.headval.nextval.nextval,"Fri")
list.delete_at_start()
list.delete_at_end()
list.listprint()    
print(list.get_count())
