import math

top = -1
st = list()
size = eval(input('Enter size of the stack: '))

def push(data):
    global top, st, size
    if (top == size - 1):
        print ('Overflow')
        return
    top += 1
    st.append(data)
    print ('Element ', data, 'added to the stack...')
    
def pop():
    global top, st
    if(top == -1):
        print ('Underflow')
        return
    ele = st[top]
    top -= 1
    print ('Element ', ele, 'removed from the stack...')
    
def displayStack():
    global top, st
    if(top == -1):
        print ('Stack is empty')
        return
    print ('The stack is: ')
    for i in range (top,-1,-1):
        print (st[i])
    
switcher = { 
        '1': push, 
        '2': pop, 
        '3': displayStack
       } 

flag = '1'

while flag != '-1':
    case = input('Enter\n1: To Push\n2: To Pop\n3: To display the stack\n')
    func = switcher.get(case)
    if case == '1':
        func(eval(input('Enter element to be pushed:  ')))
    elif case == '2' or case == '3':
        func()
    else:
        print ('Invalid choice')
        continue
    flag = input('Press ANY KEY to Continue or -1 to Exit ')

