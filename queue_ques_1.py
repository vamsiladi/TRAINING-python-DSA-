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
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size
    def check_evenly(self):
        
        for i in range(0,5):
            count=0
            for j in range(1,11):
                if self.__elements[i]%j==0:
                    count+=1
                if count==10:
                    queue2.enqueue(self.__elements[i])
                    print(self.__elements[i],end=' ')
                    
                    

                    
                    

queue1=queue(5)
queue2=queue(5)
queue1.enqueue(13983)
queue1.enqueue(10080)
queue1.enqueue(7113)
queue1.enqueue(2520)
queue1.enqueue(2500)
queue1.check_evenly()







