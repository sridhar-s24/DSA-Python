def swap(a,b):
    
    global x
    global y
    
    temp = a
    x = b
    y = temp
    print('Calling swap: ', 'X: ', x, 'Y: ', y)

x = eval(input('Enter X: '))
y = eval(input('Enter Y: '))

print('Before swap: ', 'X: ', x, 'Y: ', y)
swap(x,y)
print('After swap: ', 'X: ', x, 'Y: ', y)
