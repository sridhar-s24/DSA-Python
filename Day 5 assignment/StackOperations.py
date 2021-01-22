#Stack Operations

top = -1
St = list()
size = 5

def push(data):
    global top, St, size
    if (top == size - 1):
        print ('Overflow')
        return
    top += 1
    St.append(data)
    print ('Element ', data, 'added to the stack...')
    
def pop():
    global top, St, size
    if(top == -1):
        print ('Underflow')
        return
    ele = St[top]
    top -= 1
    print ('Element ', ele, 'removed from the stack...')    
    
def displayStack():
    global top, St, size
    if(top == -1):
        print ('List is empty')
        return
    for i in range (0, top + 1):
        print (St[i])

push(10)
push(20)
push(30)
push(40)
push(50)
displayStack()
push(60)
pop()
displayStack()
