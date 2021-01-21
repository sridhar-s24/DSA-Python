class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
                
    def displayEle(self):
        print('\n')
        if self.head == None:
            print ('List is empty')  
        else:
            temp = self.head
            while temp != None:
                print(temp.value, end = " ")
                temp = temp.next
        
    def insertFirst(self,value):
        node = Node(value)
        
        if self.head == None:
            self.head = node
        
        else:
            second = self.head
            node.next = second
            self.head = node
        
    def insertLast(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
    
    def insertByIndex(self,value,index):
            node = Node(value)
            if self.head == None:
                self.head = node
                
            elif index == 0:
                second = self.head
                node.next = second
                self.head = node
                
            else:
                temp = self.head
                for i in range(index - 1):
                    temp = temp.next
                temp2 = temp.next
                temp.next = node
                node.next = temp2
                
            
    def deleteFirst(self):
            if self.head == None:
                 print ('List is empty') 
            else:
                self.head = self.head.next
    
    def deleteLast(self):
            if self.head == None:
                 print ('List is empty') 
            else:
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
                temp.next = None
    
    def deleteByIndex(self,index):
            if self.head == None:
                 print ('List is empty') 
             
            elif index == 0:
                self.head = self.head.next
             
            else:
                temp = self.head
                for i in range(index - 1):
                    temp = temp.next
                
                temp.next = temp.next.next
    
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
            print('\n')
            temp = self.head
            if self.head == None:
                print ('List is empty')
            else:
                temp = self.head
                for i in range(middle):
                    temp = temp.next
                print('Middle element is: ', temp.value)
    
    
        
    


ll = LinkedList()
ll.insertLast(10)
ll.insertLast(20)
ll.insertLast(30)
ll.insertFirst(5)
ll.displayEle()
ll.deleteLast()
ll.displayEle()
ll.insertLast(40)
ll.insertLast(50)
ll.displayEle()
count = ll.eleCount()
ll.findMidEle(int(count/2))
ll.deleteFirst()
ll.displayEle()
ll.insertByIndex(25,2)    
ll.displayEle()
ll.deleteByIndex(3)
ll.displayEle()
        
