class queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.elements=[None]*self.max_size
        self.rear=-1
        self.front=0

    def is_full(self):
        if (self.rear==self.max_size-1):
            return True
        return False
    def is_empty(self):
        if (self.front>self.rear):
            return True
        return False
    def enqueue(self,data):
        if (self.is_full()):
            print(" queue is full!!") 
        else:
            self.rear+=1
            self.elements[self.rear]=data
    def dequeue(self):
        if (self.is_empty()):
            print("Queue is empty")
        else:
            data=self.elements[self.front]
            self.front+=1
            return data
    def display(self):
        for index in range(self.front,self.rear+1):
            print(self.elements[index],end=' ')
        print()
    def get_max_size(self):
        return self.max_size
            
        

queue1=queue(7)
queue2=queue(7)
queue3=queue(7)
print("is it full",queue1.is_full())
print("is it empty",queue1.is_empty())
queue1.enqueue(2)
#queue1.display()
queue1.enqueue(7)
queue1.enqueue(9)
queue1.enqueue(4)
#queue1.display()
queue1.enqueue(6)
queue1.enqueue(5)
queue1.enqueue(10)
queue1.display()


for i in range(queue1.front,queue1.rear+1):
    if queue1.elements[i]%2==0:
        queue2.enqueue(queue1.elements[i])
    else:
        queue3.enqueue(queue1.elements[i])

queue2.display()

queue3.display()



"""queue1.display()
print("element deleted",queue1.dequeue())
queue1.display()"""





            
                  
