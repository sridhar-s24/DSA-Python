#Queue Operations

Q = list()
capacity = 5
front = -1
rear = -1


def enqueue(data):
    global Q, capacity, front, rear
    if rear == size - 1:
        print ('Overflow')
        return
    rear += 1
    Q.append(data)
    print ('Element ', data, 'added to the queue')
    
    
def dequeue():
        global Q, capacity, front, rear
        if front == rear:
            print ('Underflow')
            return
        elem = Q[front+1]
        front += 1
        print ('Element ', elem, 'removed from the queue')
        
     
        
def displayQueue():
        global Q, capacity, front, rear
        if front == rear:
            print ('Queue is empty')
            return
        for i in range(front+1,rear+1):
            print(Q[i], end = ' ')
        print ('\n')

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
enqueue(50)
enqueue(60)
displayQueue()
dequeue()
displayQueue()
dequeue()
displayQueue()
dequeue()
displayQueue()
dequeue()
displayQueue()
dequeue()
displayQueue()
dequeue()
