class queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.elements=[None]*max_size
        self.rear=-1
        self.front=0
    def isfull(self):
        if self.rear==self.max_size-1 :
            return True
        return False
    def isempty(self):
        if self.rear<=self.front :
            return True
        return False
    def enqueue(self,data):
        if self.isfull():
            print("Queue is full")
        else:
            self.rear+=1
            self.elements[self.rear]=data
    def dequeue(self):
        if self.isempty():
            print("it is empty")
        else:
            data=self.elements[self.front]
            self.front+=1
            return data
    def display(self):
        for i in range(self.front,self.rear+1):
            data=self.elements[i]
            print(data,end=' ')
queue1=queue(10)
queue1.enqueue(7)
queue1.enqueue(28)
queue1.enqueue(8)
queue1.enqueue(35)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(5)
queue1.enqueue(15)
queue1.enqueue(2)
queue1.enqueue(5)



class stack:
    def __init__(self,max_size):
        self.max_size=max_size
        self.elements=[None]*self.max_size
        self.top=-1

    def is_full(self):
        if (self.top==self.max_size -1):
            return True
        return False
    def is_empty(self):
        if(self.top==-1):
            return True
        return False
    def push(self,data):
        if (self.is_full()):
            print("The stack is full!!")
        else:
            self.top+=1
            self.elements[self.top]=data

    def pop(self):
        if (self.is_empty()):
            print("The stack is empty")
        else:
            data=self.elements[self.top]
            self.top-=1

            return data
    def display(self):
        if (self.is_empty()):
            print("The stack is empty")

        else:
            index=self.top
            while(index>=0):
                print(self.elements[index],end=' ')
                index-=1



stack1=stack(10)
l=[]
for i in range(queue1.front,queue1.rear):
    if i%2==0:
        k=0
        
        for j in range(queue1.elements[i]+1):
            k=k+j
        if k==queue1.elements[i+1]:
            stack1.push(queue1.elements[i+1])
            
stack1.display()




