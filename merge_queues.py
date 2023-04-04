class queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if (self.__rear==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if (self.__front>self.__rear):
            return True
        return False
    def enqueue(self,data):
        if (self.is_full()):
            print(" queue is full!!") 
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if (self.is_empty()):
            print("Queue is empty")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear):
            print(self.__elements[index],end=',')
        print(self.__elements[-1])
            
    def get_max_size(self):
        return self.__max_size




l1=list(input().split(','))
l2=list(input().split(','))
queue1=queue(len(l1))
queue2=queue(len(l2))
queue3=queue(len(l1)+len(l2))

for i in l1:
    queue1.enqueue(i)
for i in l2:
    queue2.enqueue(i)

l=len(l1)+len(l2)
p=0
for i in range(l):
    if i%2==0 and p<queue1.get_max_size():
        queue3.enqueue(queue1.dequeue())
        p+=1
    else:
        queue3.enqueue(queue2.dequeue())

queue3.display()

        


