class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
        
class Compartment:
    def __init__(self):
        self.headval=None
        
        
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

    def atend(self,newdata):
        newnode=node(newdata)
        if self.headval == None:
            self.headval=newnode
        else:
            n=self.headval
            while n.nextval is not None:
                n=n.nextval
            n.nextval=newnode

    def get_count(self):
        if self.headval==None:
            return 0
        n=self.headval
        count=0
        while n is not None:
            count=count+1
            n=n.nextval
        print(count)

        






class Train:
    def __init__(self,train_name,compartment_list):
        self.train_name=train_name
        self.compartment_list=compartment_list
        


    def get_train_name(self):
        print("Train name:")
        return self.train_name


    def get_compartment_list(self):
        print("compartment_list:")
        return self.compartment_list.listprint()

    def count_compartments(self):
        print("count_compartments:",end='')
        self.compartment_list.get_count()

    def check_vacancy(self):
        n=self.compartment_list.headval
        count=0
        while n is not None:
            temp=n.dataval
            if temp[1]/temp[2]<0.50:
                count+=1
            n=n.nextval
        print("compartments with more than 50% vacancy:", +count)

compartment=Compartment()
compartment.atend(["SL",250,400])
compartment.atend(["2AC",125,280])
compartment.atend(["3AC",120,300])
compartment.atend(["FC",160,300])
compartment.atend(["1AC",100,210])         
#compartment.listprint()

train1=Train("vamsi",compartment)
print(train1.get_train_name())
train1.get_compartment_list()
train1.check_vacancy()
train1.count_compartments()
