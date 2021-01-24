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
    
def pop():
    global top, st
    if(top == -1):
        print ('Underflow')
        return
    ele = st[top]
    top -= 1
    print ('Element ', ele, 'removed from the original stack...')
    
def displayStack():
    global top, st
    if(top == -1):
        print ('Stack is empty')
        return
    print ('The original stack is: ')
    for i in range (top,-1,-1):
        print (st[i])

def getMinimum():
    global top, st2
    if(top == -1):
        print ('Stack is empty')
        return
    print ('The minimum element from the stack is: ', st2[top])

switcher = { 
        '1': push, 
        '2': pop, 
        '3': displayStack,
        '4': getMinimum,
       } 

flag = '1'

while flag != '-1':
    case = input('Enter\n1: To Push\n2: To Pop\n3: To display the stack\n4: To get minimum element\n')
    func = switcher.get(case)
    if case == '1':
        func(eval(input('Enter element to be pushed:  ')))
    elif case == '2' or case == '3' or case == '4':
        func()
    else:
        print ('Invalid choice')
        continue
    flag = input('Press ANY KEY to Continue or -1 to Exit ')
