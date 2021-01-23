import math

top = -1
st = list()
st2 = list()
size = eval(input('Enter size of the stack: '))
mini = math.inf

def push(data):
    global top, st, st2, size, mini
    if (top == size - 1):
        print ('Overflow')
        return
    top += 1
    st.append(data)
    print ('Element ', data, 'added to the original stack...')
    
    if data <= mini:
        mini = data
        st2.append(data)
    else:
        st2.append(st2[top-1]) 
        
#     print ('Element ', mini, 'added to the duplicate stack...')
       
    
def pop():
    global top, st, st2, size
    if(top == -1):
        print ('Underflow')
        return
    ele = st[top]
    top -= 1
    print ('Element ', ele, 'removed from the original stack...')

#   ele2 = st2[top]
#   print ('Element ', ele2, 'removed from the duplicate stack...')  
    
def displayStack():
    global top, st, size
    if(top == -1):
        print ('List is empty')
        return
    print ('The original stack is: ')
    for i in range (top,-1,-1):
        print (st[i])

def getMinimum():
    global st2
    print ('The minimum element from the stack is: ', st2[top])
    
        
    

push(10)
push(5)
push(20)
push(3)
push(2)
displayStack()
push(60)
pop()
displayStack()
getMinimum()
pop()
displayStack()
getMinimum()
pop()
displayStack()
getMinimum()
displayStack()
getMinimum()
