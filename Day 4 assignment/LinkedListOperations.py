class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
                
    def displayEle(self):
            if self.head == None:
                print ('List is empty')  
            else:
                temp = self.head
                while temp != None:
                    print(temp.value, end = " ")
                    temp = temp.next
                print('\n')
        
    def insertFirst(self,value):
        node = Node(value)
        
        if self.head == None:
            self.head = node
        
        else:
            second = self.head
            node.next = second
            self.head = node
        
    def deleteLast(self):
            if self.head == None:
                 print ('List is empty') 
            else:
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
                temp.next = None
    
    def eleCount(self):
            length = 0
            if self.head == None:
                print ('List is empty')  
            else:
                temp = self.head
                while temp != None:
                    temp = temp.next
                    length += 1
            return length
    
    def findMidEle(self,middle):
            temp = self.head
            if self.head == None:
                print ('List is empty')
            else:
                temp = self.head
                for i in range(middle):
                    temp = temp.next
                print('Middle element is: ', temp.value)
    
    
        
    


ll = LinkedList()
ll.insertFirst(4)
ll.insertFirst(3)
ll.insertFirst(2)
ll.insertFirst(1)
ll.displayEle()
ll.deleteLast()
ll.displayEle()
count = ll.eleCount()
ll.findMidEle(int(count/2))

        
